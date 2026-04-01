import tkinter as tk
from tkinter import ttk
import sys
import threading
import pygame
from tkinter import scrolledtext
import time
import re

run_mode = 0
current_mode = "menu"
pygame_screen = None
is_exit = False
main_win = None
text = None
undo_stack = []
redo_stack = []
last_content = ""
run_time = 0
is_optimization = 0


def enable_ui_render_optimization():
    global is_optimization
    is_optimization = 1


def set_up_rander():
    global pygame_screen, is_exit, win, current_mode, run_mode, is_optimization, setting, objects, run_time
    import os
    if pygame_screen:
        return
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = f'{screen_width // 2},25'
    pygame_screen = pygame.display.set_mode([screen_width // 2, screen_height])
    pygame.display.set_caption("Render")

    try:
        pygame.display.set_icon(pygame.image.load("logo.png"))
    except:
        pass
    clock = pygame.time.Clock()
    true_wait = 1000
    yyyy=0

    while not is_exit:
        start_time = time.time()
        pygame_screen.fill(setting["bg_color"])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_exit = True
        if current_mode != "editor":
            break
        if run_mode == 1:
            try:
                clock.tick(int(setting["fps"]))
                run_time = 0
                run_mode = -1
                true_wait = int(setting["fps"])
                yyyy = true_wait

            except:
                pass
        if run_mode == -1:
            for i in objects:
                if i["run_time"] == 0:
                    continue
                if run_time >= i["start_time"] and run_time <= i["start_time"] + i["run_time"]:
                    if i["type"] == "rect":
                        t = (run_time - i["start_time"]) / i["run_time"]
                        x = i["start_pos"][0] + (i["end_pos"][0] - i["start_pos"][0]) * t
                        y = i["start_pos"][1] + (i["end_pos"][1] - i["start_pos"][1]) * t
                        pygame.draw.rect(pygame_screen, i["bg_color"],
                                         [int(x), int(y), int(i["size"][0]), int(i["size"][1])])
                    elif i["type"] == "circle":
                        t = (run_time - i["start_time"]) / i["run_time"]
                        x = i["start_pos"][0] + (i["end_pos"][0] - i["start_pos"][0]) * t
                        y = i["start_pos"][1] + (i["end_pos"][1] - i["start_pos"][1]) * t
                        pygame.draw.circle(pygame_screen, i["bg_color"],
                                           [int(x), int(y)], radius=int(i["size"][0] / 2))
                    elif i["type"] == "text":
                        font_name = i.get("font", None)
                        if not font_name or not isinstance(font_name, str):
                            font_name = None
                        font_size = int(i["size"][0]) if i["size"][0] > 0 else 20
                        bold_value = bool(i.get("bold", False))
                        try:
                            font = pygame.font.SysFont(font_name, font_size, bold=bold_value)
                        except:
                            font = pygame.font.Font(None, font_size)
                        text_surface = font.render(i.get("text", "").strip('"'), True, i["bg_color"])
                        t = (run_time - i["start_time"]) / i["run_time"]
                        x = i["start_pos"][0] + (i["end_pos"][0] - i["start_pos"][0]) * t
                        y = i["start_pos"][1] + (i["end_pos"][1] - i["start_pos"][1]) * t
                        pygame_screen.blit(text_surface, (int(x), int(y)))

                if i.get("end_show", False) and run_time > i["start_time"] + i["run_time"]:
                    if i["type"] == "rect":
                        pygame.draw.rect(pygame_screen, i["bg_color"],
                                         [int(i["end_pos"][0]), int(i["end_pos"][1]),
                                          int(i["size"][0]), int(i["size"][1])])
                    elif i["type"] == "circle":
                        pygame.draw.circle(pygame_screen, i["bg_color"],
                                           [int(i["end_pos"][0]), int(i["end_pos"][1])],
                                           radius=int(i["size"][0] / 2))
                    elif i["type"] == "text":
                        font_name = i.get("font", None)
                        if not font_name or not isinstance(font_name, str):
                            font_name = None
                        font_size = int(i["size"][0]) if i["size"][0] > 0 else 20
                        bold_value = bool(i.get("bold", False))
                        try:
                            font = pygame.font.SysFont(font_name, font_size, bold=bold_value)
                        except:
                            font = pygame.font.Font(None, font_size)
                        text_surface = font.render(i.get("text", "").strip('"'), True, i["bg_color"])
                        pygame_screen.blit(text_surface, (int(i["end_pos"][0]), int(i["end_pos"][1])))
                if i["end_show"]==0 and run_time > i["start_time"] + i["run_time"]:
                    objects.remove(i)

            if setting["time"] > 0 and run_time >= setting["time"]:
                run_time = 0
                run_mode = 0
            run_time += 1 / int(setting["fps"])
        time.sleep(1 / true_wait)
        pygame.display.update()
        if is_optimization:
            """
            end_time = time.time()
            xxxxx = end_time - start_time
            if yyyy==0:
                pass
            elif 1/yyyy-xxxxx>0:

                true_wait = 1 / (1 / yyyy - xxxxx)
                print("new_fps:",true_wait)
                setting["fps"] = int(true_wait)
                print(true_wait)
            """



    pygame.quit()
    is_exit = False
    pygame_screen = None


def open_file():
    global text
    from tkinter import filedialog
    f = filedialog.askopenfilename(title="打开 Render 文件", filetypes=[("Python 动画渲染文件", "*.render")])
    if not f:
        return
    try:
        threading.Thread(target=switch_to_editor).start()
        time.sleep(0.5)
        with open(f, encoding="UTF-8", mode="r") as file:
            content = file.read()
            if text:
                text.delete("1.0", tk.END)
                text.insert("1.0", content)
    except Exception as e:
        print(f"打开文件失败：{e}")


def open_file1():
    switch_to_editor()
    global text
    from tkinter import filedialog
    f = filedialog.askopenfilename(title="打开 Render 文件", filetypes=[("Python 动画渲染文件", "*.render")])
    if not f:
        return
    try:
        threading.Thread(target=switch_to_editor).start()
        time.sleep(0.5)
        with open(f, encoding="UTF-8", mode="r") as file:
            content = file.read()
            if text:
                text.delete("1.0", tk.END)
                text.insert("1.0", content)
    except Exception as e:
        print(f"打开文件失败：{e}")


def save_file():
    global text
    from tkinter import filedialog
    f = filedialog.asksaveasfilename(title="保存为Render文件", filetypes=[("Python 动画渲染文件", "*.render")],
                                     defaultextension=".render")
    if f:
        with open(f, encoding="UTF-8", mode="w") as file:
            file.write(text.get("1.0", tk.END))


play_mode = "NO"
setting = {"bg_color": "#000000", "time": 0, "fps": 60}
objects = []
variables = {}


def evaluate_value(value):
    """解析值，支持变量替换、算术表达式、类型转换"""
    if not isinstance(value, str):
        return value
    value = value.strip()
    value1 = []
    for i in value:
        value1.append(i)
    for i in value1:
        if i == "`":
            if value1.index(i) != len(value1) - 1:
                if value1[value1.index(i) + 1] == "`":
                    value1[value1.index(i) + 1] = " "
                else:
                    value1[value1.index(i)] = " "
            else:
                value1[value1.index(i)] = " "
    value2 = ""
    for i in value1:
        value2 += i
    value = value2
    # 字符串原样返回
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    # 如果以 - 开头且不是颜色，可能是关键字，直接返回
    if value.startswith('-') and not value.startswith('#'):
        return value
    # 算术表达式
    if re.search(r'[+\-*/]', value) and not value.startswith('#'):
        expr = value
        for var_name, var_val in variables.items():
            expr = re.sub(r'\b' + var_name + r'\b', str(var_val), expr)
        try:
            result = eval(expr)
            if isinstance(result, float) and result.is_integer():
                return int(result)
            return result
        except Exception as e:
            print(f"Warning: evaluate_value failed for '{value}': {e}")
    # 变量名
    if value in variables:
        return variables[value]
    # 数字转换
    try:
        if '.' in value:
            return float(value)
        else:
            return int(value)
    except ValueError:
        return value


def parse_for_loop(lines, start_idx, loop_var, loop_range):
    """解析 for 循环块并展开，直接计算表达式值"""
    result_lines = []
    loop_content = []
    i = start_idx
    brace_count = 1  # 因为 for 行中已经有一个 {

    while i < len(lines):
        line = lines[i].strip()
        open_braces = line.count('{')
        close_braces = line.count('}')
        brace_count += open_braces - close_braces
        if brace_count == 0:
            i += 1  # 跳过 } 行
            break
        if line and line != '{':
            loop_content.append(line)
        i += 1

    # 展开循环
    for val in loop_range:
        old_val = variables.get(loop_var, None)
        variables[loop_var] = val
        for loop_line in loop_content:
            tokens = loop_line.split()
            new_tokens = []
            for token in tokens:
                if token == loop_var:
                    new_tokens.append(str(val))
                elif loop_var in token and any(op in token for op in '+-*/'):
                    expr = token.replace(loop_var, str(val))
                    try:
                        result = eval(expr)
                        if isinstance(result, float) and result.is_integer():
                            result = int(result)
                        new_tokens.append(str(result))
                    except Exception:
                        new_tokens.append(token)
                else:
                    evaluated = evaluate_value(token)
                    new_tokens.append(str(evaluated))
            result_lines.append(' '.join(new_tokens))
        if old_val is not None:
            variables[loop_var] = old_val
        else:
            variables.pop(loop_var, None)
    return result_lines, i


def play(line):
    global play_mode, setting, objects, variables
    words = line.split()
    if not words:
        return
    try:
        if words[0][0] == "[":
            if words[0] == "[setup]":
                play_mode = "setup"
            elif words[0] == "[object]":
                play_mode = "object"
                objects.append({
                    "start_pos": [0, 0], "end_pos": [0, 0], "bg_color": "#000000",
                    "start_time": 0, "run_time": 0, "size": [100, 100], "type": "rect",
                    "image": None, "text": "", "font": None, "bold": False, "end_show": False
                })
        elif play_mode == "setup" and words[0][0] == "-":
            if words[0] == "-bg_color":
                setting["bg_color"] = evaluate_value(words[1])
            elif words[0] == "-time":
                setting["time"] = float(evaluate_value(words[1]))
            elif words[0] == "-fps":
                setting["fps"] = int(evaluate_value(words[1]))
        elif play_mode == "object" and words[0][0] == "-":
            obj = objects[-1]
            if words[0] == "-start_pos":
                obj["start_pos"] = [float(evaluate_value(words[1])), float(evaluate_value(words[2]))]
            elif words[0] == "-end_pos":
                obj["end_pos"] = [float(evaluate_value(words[1])), float(evaluate_value(words[2]))]
            elif words[0] == "-start_time":
                obj["start_time"] = float(evaluate_value(words[1]))
            elif words[0] == "-run_time":
                obj["run_time"] = float(evaluate_value(words[1]))
            elif words[0] == "-is_bold":
                obj["bold"] = bool(int(evaluate_value(words[1])))
            elif words[0] == "-type":
                obj["type"] = str(evaluate_value(words[1]))
            elif words[0] == "-text":
                obj["text"] = str(evaluate_value(words[1]))
            elif words[0] == "-font":
                obj["font"] = str(evaluate_value(words[1]))
            elif words[0] == "-image":
                obj["image"] = str(evaluate_value(words[1]))
            elif words[0] == "-bg_color":
                obj["bg_color"] = str(evaluate_value(words[1]))
            elif words[0] == "-size":
                obj["size"] = [float(evaluate_value(words[1])), float(evaluate_value(words[2]))]
            elif words[0] == "-end_show":
                obj["end_show"] = bool(int(evaluate_value(words[1])))
    except Exception as E:
        from tkinter import messagebox
        messagebox.showerror("错误", f"解析错误：{E}")


def run():
    global text, run_mode, setting, objects, variables
    setting = {"bg_color": "#000000", "time": 0, "fps": 60}
    objects = []
    variables = {}
    users_input = text.get("1.0", tk.END)

    all_lines = [line for line in users_input.split('\n') if line.strip()]

    # 第一遍：处理 [vars] 和 for 循环
    processed_lines = []
    i = 0
    in_vars_block = False

    while i < len(all_lines):
        line = all_lines[i].strip()
        if line == "[vars]":
            in_vars_block = True
            processed_lines.append(line)
            i += 1
            continue
        elif line.startswith("[") and line != "[vars]":
            in_vars_block = False

        if in_vars_block and line.startswith("-"):
            parts = line.split()
            if len(parts) >= 2:
                var_name = parts[0][1:]
                var_value = parts[1]
                if var_value.startswith('"') and var_value.endswith('"'):
                    variables[var_name] = var_value[1:-1]
                elif var_value.startswith('#'):
                    variables[var_name] = var_value
                else:
                    try:
                        if '.' in var_value:
                            variables[var_name] = float(var_value)
                        else:
                            variables[var_name] = int(var_value)
                    except ValueError:
                        variables[var_name] = var_value
            processed_lines.append(line)
            i += 1
            continue

        # 检查 for 循环
        if line.startswith("for ") and "in range(" in line:
            match = re.match(r'for\s+(\w+)\s+in\s+range\(([^)]+)\)', line)
            if match:
                loop_var = match.group(1)
                range_str = match.group(2)
                range_parts = [int(x.strip()) for x in range_str.split(',')]
                if len(range_parts) == 1:
                    loop_range = list(range(range_parts[0]))
                elif len(range_parts) == 2:
                    loop_range = list(range(range_parts[0], range_parts[1]))
                else:
                    loop_range = list(range(range_parts[0], range_parts[1], range_parts[2]))
                expanded, next_i = parse_for_loop(all_lines, i + 1, loop_var, loop_range)
                processed_lines.extend(expanded)
                i = next_i
                continue

        processed_lines.append(line)
        i += 1

    # 第二遍：解析处理后的行
    for line in processed_lines:
        if line.strip():
            play(line)

    run_mode = 1


def switch_to_editor():
    global current_mode, main_win, text, win
    if current_mode == "editor":
        return
    a1 = win.winfo_screenwidth()
    a2 = win.winfo_screenheight()
    for widget in win.winfo_children():
        widget.destroy()

    menubar = tk.Menu(win)
    win.config(menu=menubar)
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="文件", menu=file_menu)
    file_menu.add_command(label="新建", command=switch_to_editor)
    file_menu.add_command(label="打开", command=open_file)
    file_menu.add_command(label="保存", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="退出", command=switch_to_menu)

    animation_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="动画", menu=animation_menu)
    animation_menu.add_command(label="播放", command=run)

    # UI 渲染优化菜单


    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="帮助", menu=help_menu)
    help_menu.add_command(label="关于", command=show_about)

    main_win = tk.Frame(win)
    main_win.pack(fill=tk.BOTH, expand=True)
    win.geometry(f"{a1 // 2}x{a2 - 70}+0+0")

    text = scrolledtext.ScrolledText(main_win, font=("Consolas", 15), bg='white', fg='black',
                                     wrap=tk.WORD, insertbackground='black')
    text.pack(fill=tk.BOTH, expand=True)

    toolbar = tk.Frame(main_win, bg='#F0F0F0')
    toolbar.pack(side=tk.TOP, fill=tk.X)
    tk.Button(toolbar, text="返回菜单", command=switch_to_menu).pack(side=tk.LEFT, padx=5, pady=5)
    tk.Label(toolbar, text="编辑器模式", font=("Microsoft YaHei", 12)).pack(side=tk.LEFT, padx=10)

    current_mode = "editor"
    threading.Thread(target=set_up_rander, daemon=True).start()


def switch_to_menu():
    global current_mode, main_win, pygame_screen
    if current_mode == "menu":
        return
    for widget in win.winfo_children():
        widget.destroy()
    win.geometry("800x600+100+100")
    setup_ui()
    current_mode = "menu"


def show_about():
    about_win = tk.Toplevel(win)
    about_win.title("关于")
    about_win.geometry("400x300")
    about_win.resizable(False, False)
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - 400) // 2
    y = (screen_height - 300) // 2
    about_win.geometry(f"400x300+{x}+{y}")
    content_frame = tk.Frame(about_win, bg="#F0F0F0")
    content_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(content_frame, text="Nick's Cartoon", font=("Microsoft YaHei UI", 24, "bold"),
             fg="#1E90FF", bg="#F0F0F0").pack(pady=(30, 10))
    tk.Label(content_frame, text="版本：1.0.0", font=("Microsoft YaHei", 12), bg="#F0F0F0").pack(pady=5)
    tk.Label(content_frame, text="Python 动画生成器\n支持代码编辑和实时渲染",
             font=("Microsoft YaHei", 10), bg="#F0F0F0", justify="center").pack(pady=10)
    tk.Label(content_frame, text="© 2024 Nick's Studio", font=("Microsoft YaHei", 9),
             fg="#666666", bg="#F0F0F0").pack(side=tk.BOTTOM, pady=10)
    tk.Button(content_frame, text="确定", command=about_win.destroy,
              bg="#1E90FF", fg="white", width=10).pack(pady=10)


def load_example():
    switch_to_editor()
    example_content = """[setup]
-bg_color #0a0a2a
-time 10
-fps 60

[vars]
-start_x 100
-color1 #FF3366
-color2 #33FF66
-color3 #3366FF

# 使用 for 循环创建 5 个矩形，每个间隔 100 像素
for i in range(5){
[object]
-type rect
-start_pos start_x i*100+50
-end_pos 800 i*100+50
-start_time i*0.5
-run_time 1.5
-bg_color color1
-size 80 80
-end_show 1
}

# 使用 for 循环创建 3 个圆形
for j in range(3){
[object]
-type circle
-start_pos 400 400
-end_pos j*300+200 200
-start_time 6
-run_time 2
-bg_color color2
-size 60 60
-end_show 1
}
"""
    text.delete("1.0", tk.END)
    text.insert("1.0", example_content)


def setup_ui():
    global win, main_win
    menubar = tk.Menu(win)
    win.config(menu=menubar)
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="文件", menu=file_menu)
    file_menu.add_command(label="新建", command=switch_to_editor)
    file_menu.add_command(label="打开", command=open_file1)
    file_menu.add_separator()
    file_menu.add_command(label="退出", command=switch_to_menu)
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="帮助", menu=help_menu)
    help_menu.add_command(label="关于", command=show_about)

    main_win = tk.Frame(win, width=800, height=600)
    main_win.place(x=0, y=0)
    tk.Label(main_win, text="欢迎使用 Python 动画生成器",
             font=("Microsoft YaHei UI", 32, "bold"),
             fg="#1E90FF", bg="#F0F0F0").pack(expand=True)
    button_frame = tk.Frame(main_win, bg="#F0F0F0")
    button_frame.pack(side=tk.BOTTOM, pady=30)
    tk.Button(button_frame, text="加载示例", command=load_example,
              bg="#4CAF50", fg="white", font=("Microsoft YaHei", 12), padx=20, pady=10).pack(pady=10)
    tk.Button(button_frame, text="进入编辑器", command=switch_to_editor,
              bg="#2196F3", fg="white", font=("Microsoft YaHei", 12), padx=20, pady=10).pack()


def on_closing():
    global is_exit
    is_exit = True
    win.destroy()
    win.quit()


win = tk.Tk()
win.title("Nick's Cartoon")
try:
    win.iconbitmap('logo.ico')
except:
    pass
win.geometry("800x600+100+100")
win.protocol("WM_DELETE_WINDOW", on_closing)
setup_ui()
try:
    win.mainloop()
except:
    is_exit = True
