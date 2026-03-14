# ui_theme_plugin.py
# UI 美化插件 - 完整的配色和布局修改功能

# ui_theme_plugin.py

# ui_theme_plugin.py

# UI 美化插件 - 完整的配色和布局修改功能



# ui_theme_plugin.py



# UI 美化插件 - 完整的配色和布局修改功能







import json



import os



import shutil



import re



from datetime import datetime







THEME_FILE = "theme_config.json"



BACKUP_DIR = "theme_backups"







def ui_theme_plugin(self):

    """打开主题选择器窗口"""
    import tkinter as tk

    from tkinter import ttk, colorchooser, messagebox

    import json

    app_instance=self

    # 创建主题选择器窗口

    theme_win = tk.Toplevel(app_instance.win)

    theme_win.title("🎨 UI 主题美化 - 自定义配色方案")

    theme_win.geometry("800x600+200+100")

    theme_win.configure(bg="#F0F2F5")



    # 预设主题

    preset_themes = [

        {

            "name": "默认蓝",

            "primary": "#3776AB",

            "secondary": "#7DB3C4",

            "background": "#F0F2F5",

            "text": "#333333"

        },

        {

            "name": "科技蓝",

            "primary": "#1890FF",

            "secondary": "#40A9FF",

            "background": "#E6F7FF",

            "text": "#001529"

        },

        {

            "name": "商务黑",

            "primary": "#2C3E50",

            "secondary": "#34495E",

            "background": "#ECF0F1",

            "text": "#2C3E50"

        },

        {

            "name": "清新绿",

            "primary": "#52C41A",

            "secondary": "#73D13D",

            "background": "#F6FFED",

            "text": "#237804"

        },

        {

            "name": "浪漫紫",

            "primary": "#722ED1",

            "secondary": "#9254DE",

            "background": "#F9F0FF",

            "text": "#391085"

        },

        {

            "name": "暖橙色",

            "primary": "#FA8C16",

            "secondary": "#FFC53D",

            "background": "#FFF7E6",

            "text": "#AD6800"

        },

        {

            "name": "少女粉",

            "primary": "#FF69B4",

            "secondary": "#FFB6C1",

            "background": "#FFF0F5",

            "text": "#8B0000"

        },

        {

            "name": "薄荷青",

            "primary": "#20B2AA",

            "secondary": "#48D1CC",

            "background": "#F0FFFF",

            "text": "#006994"

        }

    ]



    # 标题

    title_label = tk.Label(

        theme_win,

        text="🎨 UI 主题美化",

        font=("Microsoft YaHei", 24, "bold"),

        bg="#F0F2F5",

        fg="#333333"

    )

    title_label.pack(pady=20)



    subtitle_label = tk.Label(

        theme_win,

        text="选择预设主题或自定义配色方案",

        font=("Microsoft YaHei", 12),

        bg="#F0F2F5",

        fg="#666666"

    )

    subtitle_label.pack(pady=5)



    # 主题预览区

    preview_frame = tk.Frame(theme_win, bg="white", bd=2, relief="solid")

    preview_frame.pack(fill="x", padx=50, pady=20)



    preview_label = tk.Label(

        preview_frame,

        text="主题预览",

        font=("Microsoft YaHei", 14, "bold"),

        bg=preset_themes[0]["primary"],

        fg="white",

        pady=10

    )

    preview_label.pack(fill="x")



    preview_content = tk.Frame(preview_frame, bg=preset_themes[0]["secondary"], height=100)

    preview_content.pack(fill="both", expand=True)



    preview_btn = tk.Button(

        preview_content,

        text="预览按钮",

        font=("Microsoft YaHei", 10),

        bg=preset_themes[0]["primary"],

        fg="white",

        bd=0,

        padx=20,

        pady=5

    )

    preview_btn.place(relx=0.5, rely=0.5, anchor="center")



    # 预设主题选择区

    themes_frame = tk.Frame(theme_win, bg="#F0F2F5")

    themes_frame.pack(fill="both", expand=True, padx=50, pady=10)



    # 创建主题按钮网格

    def create_theme_buttons():

        for i, theme in enumerate(preset_themes):

            row = i // 4

            col = i % 4



            btn = tk.Button(

                themes_frame,

                text=theme["name"],

                font=("Microsoft YaHei", 10),

                bg=theme["primary"],

                fg="white",

                bd=0,

                padx=20,

                pady=10,

                command=lambda t=theme: apply_theme(t, preview_label, preview_content, preview_btn)

            )

            btn.grid(row=row, column=col, padx=10, pady=10, sticky="ew")



        themes_frame.grid_columnconfigure(0, weight=1)

        themes_frame.grid_columnconfigure(1, weight=1)

        themes_frame.grid_columnconfigure(2, weight=1)

        themes_frame.grid_columnconfigure(3, weight=1)



    create_theme_buttons()



    # 自定义颜色选择区

    custom_frame = tk.LabelFrame(

        theme_win,

        text=" 自定义配色 ",

        font=("Microsoft YaHei", 12, "bold"),

        bg="#F0F2F5",

        fg="#333333"

    )

    custom_frame.pack(fill="x", padx=50, pady=20)



    # 当前选中的主题

    current_theme = {"selected": preset_themes[0]}



    def apply_theme(theme, preview_title, preview_cnt, preview_button):

        """应用主题到预览"""

        current_theme["selected"] = theme



        # 更新预览

        preview_title.config(bg=theme["primary"])

        preview_cnt.config(bg=theme["secondary"])

        preview_button.config(bg=theme["primary"])



    # 保存按钮

    def save_theme():

        theme = current_theme["selected"]



        # 备份当前配置

        try:
            replacements = [str(theme["primary"]) + "\
", str(theme["secondary"]) + "\
",
                            str(theme["background"]) + "\
",str(theme["text"])+"\
"]
            with open("main_system.txt", 'w', encoding='utf-8') as f:
                f.writelines(replacements)
            f.close()
            self.colors= [theme["primary"],theme["secondary"],theme["background"],theme["text"]]
            self.setup_ui()
            # 替换颜色配置






        except Exception as e:

            messagebox.showerror(

                "错误",

                f"❌ 应用主题失败：{str(e)}",

                parent=theme_win

            )



    btn_frame = tk.Frame(theme_win, bg="#F0F2F5")

    btn_frame.pack(pady=20)



    save_btn = tk.Button(

        btn_frame,

        text="💾 保存并应用主题",

        font=("Microsoft YaHei", 14, "bold"),

        bg="#52C41A",

        fg="white",

        bd=0,

        padx=30,

        pady=10,

        command=save_theme

    )

    save_btn.pack(side="left", padx=10)



    cancel_btn = tk.Button(

        btn_frame,

        text="❌ 取消",

        font=("Microsoft YaHei", 12),

        bg="#D9D9D9",

        fg="#333333",

        bd=0,

        padx=20,

        pady=10,

        command=theme_win.destroy

    )

    cancel_btn.pack(side="left", padx=10)



    # 提示

    tip_label = tk.Label(

        theme_win,

        text="💡 提示：应用主题后需要重启语音助手才能看到效果",

        font=("Microsoft YaHei", 10),

        bg="#F0F2F5",

        fg="#999999"

    )

    tip_label.pack(pady=10)



def README():



    """插件说明"""



    return [False, "UI 美化插件"]







