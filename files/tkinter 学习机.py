import time
import tkinter as tk
import tkinter.messagebox as messagebox
from string import *


def original_window():
    enter_w = tk.Tk()
    enter_w.title('original_window')
    enter_w.geometry('750x500')

    lab_1 = tk.Label(enter_w, width=7, text='用户名', compound='center')
    lab_1.place(x=200, y=200)

    lab_2 = tk.Label(enter_w, width=7, text='密码', compound='center')
    lab_2.place(x=200, y=230)
    global uesr_name, password
    user_name = tk.StringVar()
    password = tk.StringVar()
    ###########获取登陆账号和密码##########
    entry = tk.Entry(enter_w, show='•', textvariable=user_name)  # 用户名
    entry.pack()
    entry.place(x=310, y=200)

    entry_1 = tk.Entry(enter_w, show="•", textvariable=password)
    # show使密码不可见
    entry_1.pack()
    entry_1.place(x=310, y=230)

    def panduan(enter_w):
        if entry.get() != 'kaixin' or entry_1.get() != '121113':
            messagebox.showerror('*_*', '密码错误,请重新输入')
        else:
            messagebox.showinfo('^_^', '密码正确,欢迎使用本软件')
            import random as r

            import turtle
            import time
            import sys
            t = turtle.Pen()
            t.penup()

            t.ht()
            t2 = turtle.Pen()
            t2.penup()

            t2.ht()
            t3 = turtle.Pen()
            t3.penup()

            t3.ht()
            t1 = turtle.Pen()
            t1.penup()

            t1.ht()
            t4 = turtle.Pen()
            t4.penup()

            t4.ht()
            t5 = turtle.Pen()
            t5.penup()

            t5.ht()
            acb = r.randint(40, 70)
            abcd = -650
            t.speed(0)
            t1.speed(0)
            t2.speed(0)
            t3.speed(0)
            t4.speed(0)
            t5.speed(0)
            turtle.tracer(130)
            for i in range(acb):
                abc = ''

                for r in range(r.randint(30, 50)):

                    s = ascii_uppercase + ascii_lowercase + digits + '////////////////////////////////'

                    ##s=str(s)
                    import random as r
                    abc += r.choice(s)

                t.clear()
                t.goto(-650, 150)
                t.write(abc, font=('Arial', 40))
                t2.penup()
                t2.goto(-650, 0)
                t2.pd()
                t2.goto(650, 0)
                t2.goto(650, -30)
                t2.goto(-650, -30)
                t2.goto(-650, 0)
                for f in range(30):
                    t2.goto(-650, 0 - f)
                    t2.goto(abcd + 1300 / acb, 0 - f)
                t1.penup()
                t1.goto(-650, 0)
                t1.pd()
                t1.goto(650, 0)
                t1.goto(650, -30)
                t1.goto(-650, -30)
                t1.goto(-650, 0)
                for f in range(30):
                    t1.goto(-650, -30 + f)
                    t1.goto(abcd + 1300 / acb, -30 + f)
                t3.penup()
                t3.goto(-650, 0)
                t3.pd()
                t3.goto(650, 0)
                t3.goto(650, -30)
                t3.goto(-650, -30)
                t3.goto(-650, 0)
                for f in range(15):
                    t3.goto(-650, -15 + f)
                    t3.goto(abcd + 1300 / acb, -15 + f)
                t4.penup()
                t4.goto(-650, 0)
                t4.pd()
                t4.goto(650, 0)
                t4.goto(650, -30)
                t4.goto(-650, -30)
                t4.goto(-650, 0)
                for f in range(15):
                    t4.goto(-650, -15 - f)
                    t4.goto(abcd + 1300 / acb, -15 - f)
                t5.penup()
                t5.goto(-650, 0)
                t5.pd()
                t5.goto(650, 0)
                t5.goto(650, -30)
                t5.goto(-650, -30)
                t5.goto(-650, 0)
                for f in range(7):
                    t5.goto(-650, -23 - f)
                    t5.goto(abcd + 1300 / acb, -23 - f)
                abcd += 1300 / acb
                time.sleep(0.00001)
                t2.penup()
                t1.penup()
                t3.penup()
                t4.penup()
                t5.penup()
            t.clear()
            t1.clear()
            t2.clear()
            t3.clear()
            t4.clear()
            t5.clear()
            t.goto(-90, 20)
            t.write("加载完成！", font=(None, 40))
            turtle.clone()
            import tkinter as tk
            import happy
            import tkinter.font as tkFont
            import tkinter.messagebox
            import random as r
            import pygame

            aaa = ""
            yw = 4
            daan = ["2:3,4:9", "6", "0.06", "90,180", "28", "4,圆心"]
            win = happy.esay.init_tkinter("学习机", 750, 500)
            pygame.init()
            pygame.mixer.init()
            sound = []
            a = pygame.mixer.Sound("recording2.wav")
            sound.append(a)
            a = pygame.mixer.Sound("2.wav")
            sound.append(a)
            a = pygame.mixer.Sound("recording1.wav")
            sound.append(a)
            a = pygame.mixer.Sound("21.wav")
            sound.append(a)

            def transformation_my(e, e1, e2):
                e = e.get()
                e1 = e1.get()
                e2 = e2.get()
                happy.file.image.transformation_image(e, e1, e2)
                print("done")

            def make_qr():
                import qrcode as qr
                win_txt = happy.esay.init_tkinter("二维码", 800, 600)
                user_nam = tk.StringVar()
                nei = tk.Label(win_txt, text="内容:")
                ne = tk.Label(win_txt, text="文件名:")

                na = tk.StringVar()
                tx = tk.Entry(win_txt, textvariable=user_nam, width=850)
                tx.pack()
                tx.place(x=50, y=0)
                tn = tk.Entry(win_txt, textvariable=na, width=850)
                tn.pack()
                tn.place(x=50, y=50)
                nw = tk.StringVar()

                tk.Label(win_txt, text="(换行请打“/”)").place(y=150, x=120)

                def ti():

                    r_txt = tx.get()
                    name = tn.get()
                    nei = []
                    for i in r_txt:

                        if i == "/":
                            nei.append("\n")
                        else:
                            nei.append(i)
                    neirong = happy.Math.print_list(nei).print_list()
                    name = tn.get()

                    img = qr.make(neirong)
                    img.save(name + ".png")

                t = tk.Button(win_txt, text="确认", compound="center", command=lambda: ti())
                t.pack()
                t.place(x=50, y=200)
                nei.pack()
                nei.place(x=0, y=0)

                ne.pack()
                ne.place(x=0, y=50)

            def docx():
                win_txt = happy.esay.init_tkinter("docx", 800, 600)
                user_nam = tk.StringVar()
                nei = tk.Label(win_txt, text="内容:")
                ne = tk.Label(win_txt, text="文件名:")
                wn = tk.Label(win_txt, text="路径:")
                na = tk.StringVar()
                tx = tk.Entry(win_txt, textvariable=user_nam, width=850)
                tx.pack()
                tx.place(x=50, y=0)
                tn = tk.Entry(win_txt, textvariable=na, width=850)
                tn.pack()
                tn.place(x=50, y=50)
                nw = tk.StringVar()
                tw = tk.Entry(win_txt, textvariable=nw, width=850)
                tw.pack()
                tw.place(x=50, y=100)

                def call_button():
                    tw.delete(0, tk.END)
                    tw.insert(0, "F:\\陈九霖\\陈九霖\\编程\\python\\Pythonlearning\\tkinter_learning\\my\\")

                button_where = tk.Button(win_txt, text="本文件夹", command=call_button)
                button_where.place(y=150, x=0)

                def call_button1():
                    tw.delete(0, tk.END)
                    tw.insert(0, "C:\\Users\\Windows\\Desktop\\")

                button_where1 = tk.Button(win_txt, text="桌面", command=call_button1)
                button_where1.place(y=150, x=70)
                tk.Label(win_txt, text="(换行请打“/”)").place(y=150, x=120)

                def ti():
                    where = tw.get()
                    r_txt = tx.get()
                    name = tn.get()
                    nei = []
                    for i in r_txt:

                        if i == "/":
                            nei.append("\n")
                        else:
                            nei.append(i)
                    neirong = happy.Math.print_list(nei).print_list()
                    name = tn.get()
                    f = where + name + ".docx"
                    txt_file = open(f, "w")
                    txt_file.write(neirong)

                t = tk.Button(win_txt, text="确认", compound="center", command=lambda: ti())
                t.pack()
                t.place(x=50, y=200)
                nei.pack()
                nei.place(x=0, y=0)

                ne.pack()
                ne.place(x=0, y=50)
                wn.pack()
                wn.place(x=0, y=100)

            def txt():
                win_txt = happy.esay.init_tkinter("txt", 800, 600)
                user_nam = tk.StringVar()
                nei = tk.Label(win_txt, text="内容:")
                ne = tk.Label(win_txt, text="文件名:")
                wn = tk.Label(win_txt, text="路径:")
                na = tk.StringVar()
                tk.Label(win_txt, text="(换行请打“/”)").place(y=150, x=120)
                tx = tk.Entry(win_txt, textvariable=user_nam, width=850)
                tx.pack()
                tx.place(x=50, y=0)
                tn = tk.Entry(win_txt, textvariable=na, width=850)
                tn.pack()
                tn.place(x=50, y=50)
                nw = tk.StringVar()
                tw = tk.Entry(win_txt, textvariable=nw, width=850)
                tw.pack()
                tw.place(x=50, y=100)

                def call_button():
                    tw.delete(0, tk.END)
                    tw.insert(0, "F:\\陈九霖\\陈九霖\\编程\\python\\Pythonlearning\\tkinter_learning\\my\\")

                button_where = tk.Button(win_txt, text="本文件夹", command=call_button)
                button_where.place(y=150, x=0)

                def call_button1():
                    tw.delete(0, tk.END)
                    tw.insert(0, "C:\\Users\\Windows\\Desktop\\")

                button_where1 = tk.Button(win_txt, text="桌面", command=call_button1)
                button_where1.place(y=150, x=70)

                def ti():
                    where = tw.get()
                    r_txt = tx.get()
                    nei = []
                    for i in r_txt:

                        if i == "/":
                            nei.append("\n")
                        else:
                            nei.append(i)
                    neirong = happy.Math.print_list(nei).print_list()
                    name = tn.get()
                    f = where + name + ".txt"
                    txt_file = open(f, "w")
                    txt_file.write(neirong)

                t = tk.Button(win_txt, text="确认", compound="center", command=lambda: ti())
                t.pack()
                t.place(x=50, y=200)
                nei.pack()
                nei.place(x=0, y=0)

                ne.pack()
                ne.place(x=0, y=50)
                wn.pack()
                wn.place(x=0, y=100)

            def mx():
                w_mx = happy.esay.init_tkinter("补充古诗", 900, 200)
                q = tk.StringVar()
                q.set("题目：")

                t = tk.Label(w_mx, textvariable=q, width=50)
                t.pack()
                t.place(x=0, y=0)
                user_nam = tk.StringVar()

                user_nam1 = tk.StringVar()
                user_nam2 = tk.StringVar()
                z = tk.Label(w_mx, text="题目：")
                z_z = tk.Label(w_mx, text="正文：")
                z_y = tk.Label(w_mx, text="诗人：")
                e = tk.Entry(w_mx, textvariable=user_nam, width=850)
                e.pack()
                e.place(x=50, y=0)
                en = tk.Entry(w_mx, textvariable=user_nam1, width=100)
                en.pack()
                en.place(x=50, y=100)
                entry = tk.Entry(w_mx, textvariable=user_nam2, width=850)  # 用户名
                entry.pack()
                entry.place(x=50, y=50)

                def zuhe():
                    nei = []
                    neirong = entry.get()
                    nei.append("《" + e.get() + "》")
                    nei.append("  ")
                    nei.append(en.get() + "\n")
                    for i in neirong:
                        nei.append(i)
                        if i == "，" or i == "。" or i == "！" or i == "？":
                            nei.append("\n")

                    neirong = happy.Math.print_list(nei).print_list()
                    cc("7", neirong)

                btn = tk.Button(w_mx, text="提交", fg="black", compound='center',
                                bg="yellow",
                                command=lambda: zuhe())

                btn.pack()
                btn.place(x=870, y=0)
                z.pack()
                z.place(x=0, y=0)
                z_z.pack()
                z_z.place(x=0, y=50)
                z_y.pack()
                z_y.place(x=0, y=100)

            def cc(name, n):
                d = "F:\\陈九霖\\陈九霖\\编程\\python\\Pythonlearning\\tkinter_learning\\my\\"
                f = d + name + ".txt"
                file = open(f, "w")
                file.write(n)

            def math(name):
                winm = happy.esay.init_tkinter("数学", 750, 120)

                name = str(name)
                with open("s" + name + ".txt", encoding="utf_8") as poem1:
                    poem1s = poem1.readlines()
                font1 = tkFont.Font(family="楷体", size=22, weight=tkFont.BOLD, slant=tkFont.ITALIC, underline=True
                                    )
                for line in poem1s:
                    line = line.strip("\n")
                    tk.Label(winm, text=line, font=font1, bg="yellow", padx=1000).pack()
                xiti("答案：", 150, 50, winm)
                shuru(200, 50, winm, "提交", name)

            def h(pic_a):
                pic1 = tk.PhotoImage(file="1.png")
                pic = tk.Label(win, image=pic1).pack()
                win.title("化学")
                win.mainloop()

            def chinese(name, sound_lst):
                winc = happy.esay.init_tkinter("语文", 750, 120)

                if name > 4:
                    name = str(name)
                    with open(name + ".txt", encoding="ANSI") as poem:
                        poems = poem.readlines()
                        font1 = tkFont.Font(family="楷体", size=22, weight=tkFont.BOLD, slant=tkFont.ITALIC,
                                            underline=True)
                    for line in poems:
                        line = line.strip("\n")
                        tk.Label(winc, text=line, font=font1, bg="yellow", padx=1000).pack()
                else:
                    name = str(name)
                    with open(name + ".txt", encoding="utf_8") as poem:
                        poems = poem.readlines()
                        font1 = tkFont.Font(family="楷体", size=22, weight=tkFont.BOLD, slant=tkFont.ITALIC,
                                            underline=True)
                    for line in poems:
                        line = line.strip("\n")
                        tk.Label(winc, text=line, font=font1, bg="yellow", padx=1000).pack()

            # 字体
            def xiti(name, x, y, win):
                font = tkFont.Font(family="楷体", size=22, weight=tkFont.BOLD, slant=tkFont.ITALIC,
                                   overstrike=False)
                lab_1 = tk.Label(win, text=name, font=font, bg="yellow", compound='center')
                lab_1.place(x=x, y=y)

            def shuru(x, y, enter_w, text, name):
                user_name = tk.StringVar()
                entry = tk.Entry(enter_w, textvariable=user_name)  # 用户名
                entry.pack()
                entry.place(x=x, y=y)

                # 按键

                def panduan(enter_w, text, name):
                    name = int(name)
                    if entry.get() != daan[name - 1]:

                        tk.messagebox.showerror('*_*', '答错啦！')
                    else:
                        tk.messagebox.showinfo('^_^', '答对啦！')
                        d = 1
                        return d

                btn = tk.Button(enter_w, text=text, fg="black", width=7, compound='center',
                                bg="yellow", command=lambda: panduan(enter_w, text, name))
                btn.pack()
                btn.place(x=x + 120, y=y - 5)

            def button(enter_w, text, x, y):
                btn = tk.Button(enter_w, text=text, fg="black", compound='center',
                                bg="yellow",
                                command=lambda: chinese(r.randint(1, 5), sound))

                btn.pack()
                btn.place(x=x, y=y)

            def button_s(enter_w, text, x, y):
                btn1 = tk.Button(enter_w, text=text, fg="black", compound='center',
                                 bg="yellow",
                                 command=lambda: math(r.randint(1, 6)))

                btn1.pack()
                btn1.place(x=x, y=y)

            def button_h(enter_w, text, x, y):
                btn2 = tk.Button(enter_w, text=text, fg="black", compound='center',
                                 bg="yellow",
                                 command=lambda: h(pic_h))

                btn2.pack()
                btn2.place(x=x, y=y)

            def button_cc(enter_w, text, x, y):
                btn2 = tk.Button(enter_w, text=text, fg="black", compound='center',
                                 bg="yellow",
                                 command=lambda: mx())

                btn2.pack()
                btn2.place(x=x, y=y)

            def button_a(enter_w, text, x, y):
                btn5 = tk.Button(enter_w, text=text, fg="black", compound='center',
                                 bg="yellow",
                                 command=lambda: ask())
                btn5.pack()
                btn5.place(x=x, y=y)

            def ask():
                import qrcode
                import happy
                import pygame
                import random
                a_p = random.randint(100000, 999999)
                a_p = str(a_p)
                img = qrcode.make("验证码：" + a_p)
                img.save("ewm.png")

                s = happy.esay.init(330, 330, "获取验证码")
                a = happy.esay.load_pic("ewm.png")
                b = 0
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            b = 1
                    if b == 1:
                        break
                    happy.esay.blit(0, 0, a, s)
                    pygame.display.update()
                win_ask = happy.esay.init_tkinter("验证", 150, 50)
                user = tk.StringVar()
                entry3 = tk.Entry(win_ask, textvariable=user, width=40)  # 用户名
                entry3.pack()
                entry3.place(x=0, y=0)

                # 按键

                def p(n):

                    if entry3.get() != n:

                        tk.messagebox.showerror('*_*', '答错啦！')
                    else:
                        tk.messagebox.showinfo('^_^', '答对啦！')
                        # 飞机大战
                        import pygame, random, sys

                        # 初始设置
                        pygame.init()
                        width, height = 480, 750  # 窗口长和宽
                        bg_y = 0  # 背景图初始Y坐标
                        bg2_y = -height
                        # 设置主角坐标
                        player_x = 240
                        player_y = 750 - 62
                        # 记录按键状态
                        keys = [0, 0]  # 左右移动
                        # 子弹数据
                        bullets = []
                        timer = 10
                        # 敌人数据
                        enemy = []  # [x,y,helth,type,speed](坐标，血量，外形，速度)
                        small = 100
                        middle = 300
                        big = 1000

                        # 导入图片
                        bg = pygame.image.load("background.png")  # 背景
                        bg2 = pygame.image.load("background.png")

                        bg = pygame.transform.scale(bg, (width, height))  # 调整背景图片大小
                        bg2 = pygame.transform.scale(bg2, (width, height))

                        player = pygame.image.load("hero1.png")  # 自己
                        enemy1 = pygame.image.load("enemy1.png")  # 敌人
                        enemy2 = pygame.image.load("enemy2.png")
                        enemy3 = pygame.image.load("enemy3.png")
                        bullet = pygame.image.load("bullet1.png")

                        # 导入声音
                        pygame.mixer.init()
                        pygame.mixer.music.load("bgm.mp3")
                        boom = pygame.mixer.Sound("boom.mp3")
                        biu = pygame.mixer.Sound("biu.mp3")
                        gameover = pygame.mixer.Sound("gameover.mp3")

                        pygame.mixer.music.play(-1)

                        screen = pygame.display.set_mode((width, height))
                        pygame.display.set_caption("飞机大战")
                        t = 0
                        while True:
                            if t == 1:
                                break
                            screen.blit(bg, (0, bg_y))  # 将背景图传输到窗口上显示
                            screen.blit(bg2, (0, bg2_y))
                            # 生成子弹
                            timer -= 1
                            if timer <= 0:
                                bullets.append([player_x, player_y])
                                bullets.append([player_x + 20, player_y])
                                bullets.append([player_x - 20, player_y])
                                biu.set_volume(0.1)
                                biu.play()
                                timer = 10
                            # 发射子弹
                            for pos in bullets:
                                bulletRect = bullet.get_rect()
                                bulletRect.center = pos
                                screen.blit(bullet, bulletRect)
                                pos[1] -= 5

                            # 设置主角中心点
                            playerRect = player.get_rect()
                            playerRect.center = (player_x, player_y)
                            screen.blit(player, playerRect)
                            # 根据按键状态移动主角
                            if keys[0] and player_x > 50:
                                player_x -= 4
                            elif keys[1] and player_x < width - 50:
                                player_x += 4

                            bg_y += 1  # 向下移动
                            bg2_y += 1

                            # 生成敌人
                            small -= 1
                            middle -= 1
                            big -= 1
                            if small <= 0:  # 生成小敌人
                                enemy.append([random.randint(0, width - 57), 0, 3, enemy1, 2])
                                small = 100
                            if middle <= 0:  # 生成中敌人
                                enemy.append([random.randint(0, width - 69), 0, 7, enemy2, 1])
                                middle = 300
                            if big <= 0:  # 生成大敌人
                                enemy.append([random.randint(0, width - 169), 0, 20, enemy3, 0.5])
                                big = 1000
                            # 出现敌人
                            for data in enemy:
                                screen.blit(data[3], (data[0], data[1]))
                                data[1] += data[4]
                                # 敌人移出屏幕
                                if data[1] > height:
                                    enemy.remove(data)
                                # 获取敌人图片的矩形区域
                                if data[3] == enemy1:  # 小敌人
                                    enemyRect = enemy1.get_rect()
                                    enemyRect.topleft = [data[0], data[1]]
                                elif data[3] == enemy2:  # 中敌人
                                    enemyRect = enemy2.get_rect()
                                    enemyRect.topleft = [data[0], data[1]]
                                elif data[3] == enemy3:  # 大敌人
                                    enemyRect = enemy3.get_rect()
                                    enemyRect.topleft = [data[0], data[1]]
                                # 判断敌人碰到主角
                                if enemyRect.colliderect(playerRect):
                                    gameover.play()
                                    pygame.quit()  # 游戏结束
                                    sys.exit()

                                # 遍历子弹列表
                                for zidan in bullets:
                                    bulletRect = bullet.get_rect()  # 获取子弹矩形区域
                                    bulletRect.center = zidan  # 设置子弹矩形中心坐标
                                    if enemyRect.colliderect(bulletRect):
                                        data[2] -= 1  # 敌人血量减少
                                        bullets.remove(zidan)  # 子弹移除
                                if data[2] <= 0:
                                    enemy.remove(data)
                                    boom.set_volume(0.5)
                                    boom.play()

                            if bg_y >= height:  # 移除屏幕后重新回到顶部
                                bg_y = -height

                            if bg2_y >= height:
                                bg2_y = -height

                            # 处理事件
                            for event in pygame.event.get():
                                # 退出
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    t = 1
                                # 按下按键
                                if event.type == pygame.KEYDOWN:
                                    # 检测具体哪一个按键
                                    if event.key == pygame.K_a or \
                                            event.key == pygame.K_LEFT:  # a键或者左移键
                                        keys[0] = 1
                                    if event.key == pygame.K_d or \
                                            event.key == pygame.K_RIGHT:  # d键或者右移键
                                        keys[1] = 1
                                # 松开按键
                                if event.type == pygame.KEYUP:
                                    # 检测具体哪一个按键
                                    if event.key == pygame.K_a or \
                                            event.key == pygame.K_LEFT:  # a键或者左移键
                                        keys[0] = 0
                                    if event.key == pygame.K_d or \
                                            event.key == pygame.K_RIGHT:  # d键或者右移键
                                        keys[1] = 0

                            pygame.display.update()

                btn = tk.Button(win_ask, text="提交", fg="black", width=7, compound='center',
                                bg="yellow", command=lambda: p(a_p))
                btn.pack()
                btn.place(x=100, y=0)

            def button_docx():
                btn5 = tk.Button(win, text="写一个docx文件", fg="black", bg="yellow", compound="center",
                                 command=lambda: docx())
                btn5.pack()
                btn5.place(x=400, y=200)

            def button_txt():
                btn5 = tk.Button(win, text="写一个txt文件", fg="black", bg="yellow", compound="center",
                                 command=lambda: txt())
                btn5.pack()
                btn5.place(x=300, y=200)

            def text_my():
                import tkinter as tk

                def s(e, e2):
                    a = open(e2.get() + e.get() + ".docx", mode="w")
                    a.write(text.get("1.0", tk.END))

                def insert(e2):
                    e2.delete(0, tk.END)
                    e2.insert(0, "C:\\Users\\Windows\\Desktop\\")

                def insert_my(e2):
                    e2.delete(0, tk.END)
                    e2.insert(0, "F:\\陈九霖\\陈九霖\\编程\\python\\Pythonlearning\\tkinter_learning\\my\\")

                def save():
                    win_s = tk.Tk()
                    win_s.geometry("220x200")
                    sl = tk.Label(win_s, text="文件名：")
                    e = tk.Entry(win_s, width=170)
                    b1 = tk.Button(win_s, text="保存", command=lambda: s(e, e2))
                    e2 = tk.Entry(win_s, width=170)
                    l2 = tk.Label(win_s, text="路径：")
                    b2 = tk.Button(win_s, text="桌面", command=lambda: insert(e2))
                    b3 = tk.Button(win_s, text="本文件夹", command=lambda: insert_my(e2))
                    sl.place(x=0, y=0)
                    e.place(x=50, y=0)
                    b1.pack(side=tk.BOTTOM)
                    e2.place(x=50, y=50)
                    l2.place(x=0, y=50)
                    b2.place(x=0, y=100)
                    b3.place(x=50, y=100)

                win = tk.Tk()

                frame = tk.Frame(win)
                scrollbar_x = tk.Scrollbar(frame, orient="horizontal")
                scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
                b = tk.Button(win, text="保存(s)", command=save)
                b.pack(anchor="nw")

                frame.pack(side=tk.BOTTOM)
                scrollbar = tk.Scrollbar(frame)
                scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                text = tk.Text(frame, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar_x.set, width=82)
                text.pack()
                scrollbar_x.config(command=text.xview)

                scrollbar.config(command=text.yview)

            def open_pic():
                def open_my():
                    aaaaaaa = e.get()
                    pic = Image.open(aaaaaaa)

                    pic.show()
                    breakpoint(pic)

                from PIL import Image
                import happy
                win_o = happy.esay.init_tkinter("open", 300, 200)
                tk.Label(win_o, text="路径+图片：").place(x=0, y=0)
                e = tk.Entry(win_o, width=230)
                e.place(x=70, y=0)
                tk.Button(win_o, text="ok", command=open_my).place(x=0, y=30)

            def open_text():
                def open_text_my():
                    go = 1
                    aaaaaaa = e.get()
                    aaaaaaaa = []
                    try:
                        with open(aaaaaaa) as poem:
                            aaaaaaaa = poem.read()
                    except:
                        go = 0
                        print("找不带该文件！")
                    # for line in poems:
                    #   aaaaaaaa.append(line)
                    # aaaaaaaa = happy.Math(aaaaaaaa).print_list()
                    import tkinter as tk
                    def s(e, e2):
                        try:
                            a = open(e2.get() + e.get() + ".docx", mode="w")
                            a.write(text.get("1.0", tk.END))
                        except:
                            import os
                            os.remove(e2.get() + e.get() + ".docx")

                    def insert(e2):
                        e2.delete(0, tk.END)
                        e2.insert(0, "C:\\Users\\Windows\\Desktop\\")

                    def insert_my(e2):
                        e2.delete(0, tk.END)
                        e2.insert(0, "F:\\陈九霖\\陈九霖\\编程\\python\\Pythonlearning\\tkinter_learning\\my\\")

                    def save():
                        win_s = tk.Tk()
                        win_s.geometry("220x200")
                        sl = tk.Label(win_s, text="文件名：")
                        e = tk.Entry(win_s, width=170)
                        b1 = tk.Button(win_s, text="保存", command=lambda: s(e, e2))
                        e2 = tk.Entry(win_s, width=170)
                        l2 = tk.Label(win_s, text="路径：")
                        b2 = tk.Button(win_s, text="桌面", command=lambda: insert(e2))
                        b3 = tk.Button(win_s, text="本文件夹", command=lambda: insert_my(e2))
                        sl.place(x=0, y=0)
                        e.place(x=50, y=0)
                        b1.pack(side=tk.BOTTOM)
                        e2.place(x=50, y=50)
                        l2.place(x=0, y=50)
                        b2.place(x=0, y=100)
                        b3.place(x=50, y=100)

                    if go == 1:
                        win = tk.Tk()
                        frame = tk.Frame(win)
                        frame.pack(side="bottom")
                        tk.Button(win, text="save", command=save).pack(anchor="nw")
                        scrollbar = tk.Scrollbar(frame)
                        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                        scrollbar_x = tk.Scrollbar(frame, orient="horizontal")
                        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
                        text = tk.Text(frame, xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar.set,
                                       wrap=tk.NONE)
                        text.pack(fill=tk.X)
                        scrollbar.config(command=text.yview)
                        scrollbar_x.config(command=text.xview)

                        text.insert("1.0", aaaaaaaa)

                import happy
                win_text = happy.esay.init_tkinter("open", 300, 200)
                tk.Label(win_text, text="路径+文本：").place(x=0, y=0)
                e = tk.Entry(win_text, width=230)
                e.place(x=70, y=0)
                tk.Button(win_text, text="ok", command=open_text_my).place(x=0, y=30)

            def del_my():
                import os
                import os.path
                aaa = input("文件路径：")
                try:
                    aa = os.path.isdir(aaa)
                except:
                    print("找不到该文件！")
                if aa == True:

                    import shutil
                    def is_empty_folder(path):
                        if os.path.isdir(path):
                            return not os.listdir(path)
                        else:
                            return False

                    a = is_empty_folder(aaa)
                    if a == True:
                        os.rmdir(aaa)
                    if a == False:
                        shutil.rmtree(aaa)
                else:
                    os.remove(aaa)
                print("done")

            def calculated():
                import happy
                import tkinter as tk

                win = tk.Tk()
                win.geometry("440x245")

                buttons = ["C", "←", "÷", "*", "-", "7", "8", "9", "(", ")", "4", "5", "6", "+", "=", "1", "2", "3",
                           "0", "."]
                buttons_use = []
                t = -1
                frame = tk.Frame(win)
                frame.pack(side=tk.BOTTOM)
                win.title("计算器")
                aaa = ""

                def button1(a111):
                    global aaa
                    if a111 == "²":
                        aaaaa = float(aaa[-1])
                        aaa = happy.Math.destroy_str(aaa)
                        aaa.remove(aaa[-1])

                        aaa = aaa.insert(aaa[-1], str(aaaaa * aaaaa))
                        aaa = happy.Math.print_list(aaa)
                    if a111 == "÷":
                        aaa = aaa + "/"

                    if a111 == "x":
                        aaa = aaa + "*"

                    if a111 != "x" and a111 != "÷" and a111 != "C" and a111 != "←" and a111 != "=" and a111 != "²":
                        aaa = aaa + a111

                    if a111 == "←":
                        aaaa = []
                        if len(aaa) > 0:
                            for i in range(len(aaa) - 1):
                                aaaa.append(aaa[i])
                            aaa = happy.Math.print_list(aaaa)
                            e = tk.Label(win, text=aaa + " ", font=(None, 30))
                            e.place(x=0, y=0)
                    if a111 == "C":
                        aaa = ""
                        e = tk.Label(win, text="\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",
                                     font=(None, 30))
                        e.place(x=0, y=0)
                    if a111 != "C" and a111 != "←" and a111 != "=":
                        e = tk.Label(win, text=aaa, font=(None, 30))
                        e.place(x=0, y=0)

                    if a111 == "=":

                        if aaa != "":

                            aaa = str(happy.Math.get_math(aaa))
                            e = tk.Label(win, text=aaa + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",
                                         font=(None, 30))
                            e.place(x=0, y=0)
                        else:
                            aaa = str(0)
                            e = tk.Label(win, text=aaa + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",
                                         font=(None, 30))
                            e.place(x=0, y=0)

                def button2():
                    e = input("你的方程是：")
                    e = happy.Math.get_equation(e)
                    print(e)

                def go():
                    a = tk.Button(frame, text=buttons[0], width=9, command=lambda: button1(buttons[0]))
                    a.grid(row=0, column=0, padx=4, pady=4)
                    a1 = tk.Button(frame, text=buttons[1], width=9, command=lambda: button1(buttons[1]))
                    a1.grid(row=0, column=1, padx=4, pady=4)
                    a2 = tk.Button(frame, text=buttons[2], width=9, command=lambda: button1(buttons[2]))
                    a2.grid(row=0, column=2, padx=4, pady=4)
                    a3 = tk.Button(frame, text=buttons[3], width=9, command=lambda: button1(buttons[3]))
                    a3.grid(row=0, column=3, padx=4, pady=4)
                    a4 = tk.Button(frame, text=buttons[4], width=9, command=lambda: button1(buttons[4]))
                    a4.grid(row=0, column=4, padx=4, pady=4)
                    a5 = tk.Button(frame, text=buttons[5], width=9, command=lambda: button1(buttons[5]))
                    a5.grid(row=1, column=0, padx=4, pady=4)
                    a6 = tk.Button(frame, text=buttons[6], width=9, command=lambda: button1(buttons[6]))
                    a6.grid(row=1, column=1, padx=4, pady=4)
                    a7 = tk.Button(frame, text=buttons[7], width=9, command=lambda: button1(buttons[7]))
                    a7.grid(row=1, column=2, padx=4, pady=4)
                    a8 = tk.Button(frame, text=buttons[8], width=9, command=lambda: button1(buttons[8]))
                    a8.grid(row=1, column=3, padx=4, pady=4)
                    a9 = tk.Button(frame, text=buttons[9], width=9, command=lambda: button1(buttons[9]))
                    a9.grid(row=1, column=4, padx=4, pady=4)
                    a10 = tk.Button(frame, text=buttons[10], width=9, command=lambda: button1(buttons[10]))
                    a10.grid(row=2, column=0, padx=4, pady=4)
                    a11 = tk.Button(frame, text=buttons[11], width=9, command=lambda: button1(buttons[11]))
                    a11.grid(row=2, column=1, padx=4, pady=4)
                    a12 = tk.Button(frame, text=buttons[12], width=9, command=lambda: button1(buttons[12]))
                    a12.grid(row=2, column=2, padx=4, pady=4)
                    a13 = tk.Button(frame, text=buttons[13], width=9, command=lambda: button1(buttons[13]))
                    a13.grid(row=2, column=3, padx=4, pady=4)
                    a14 = tk.Button(frame, text=buttons[14], width=9, command=lambda: button1(buttons[14]))
                    a14.grid(row=2, column=4, padx=4, pady=4)
                    a15 = tk.Button(frame, text=buttons[15], width=9, command=lambda: button1(buttons[15]))
                    a15.grid(row=3, column=0, padx=4, pady=4)
                    a16 = tk.Button(frame, text=buttons[16], width=9, command=lambda: button1(buttons[16]))
                    a16.grid(row=3, column=1, padx=4, pady=4)
                    a17 = tk.Button(frame, text=buttons[17], width=9, command=lambda: button1(buttons[17]))
                    a17.grid(row=3, column=2, padx=4, pady=4)
                    a18 = tk.Button(frame, text=buttons[18], width=9, command=lambda: button1(buttons[18]))
                    a18.grid(row=3, column=3, padx=4, pady=4)
                    a19 = tk.Button(frame, text=buttons[19], width=9, command=lambda: button1(buttons[19]))
                    a19.grid(row=3, column=4, padx=4, pady=4)
                    a20 = tk.Button(frame, text="π", width=9, command=lambda: button1(str(happy.Math.pi)))
                    a20.grid(row=4, column=0, padx=4, pady=4)
                    a20 = tk.Button(frame, text="e", width=9, command=lambda: button1(str(happy.Math.e)))
                    a20.grid(row=4, column=1, padx=4, pady=4)
                    a21 = tk.Button(frame, text="**", width=9, command=lambda: button1("**"))
                    a21.grid(row=4, column=2, padx=4, pady=4)
                    a21 = tk.Button(frame, text="y", width=9,
                                    command=lambda: button1(str(0.577215664901532860)))

                    a21.grid(row=4, column=3, padx=4, pady=4)
                    a21 = tk.Button(frame, text="解方程模式", width=9,
                                    command=lambda: button2())

                    a21.grid(row=4, column=4, padx=4, pady=4)

                    win.mainloop()

                go()

            def transformation():
                aa = happy.esay.init_tkinter("格式转换", 300, 200)
                tk.Label(aa, text="image:").place(x=0, y=0)
                e = tk.Entry(aa, width=250)
                e.place(x=50, y=0)
                tk.Label(aa, text="初始格式：").place(x=0, y=50)
                e1 = tk.Entry(aa, width=250)
                e1.place(x=50, y=50)
                tk.Label(aa, text="目标格式：").place(x=0, y=100)
                e2 = tk.Entry(aa, width=250)
                e2.place(x=50, y=100)
                tk.Button(aa, text="ok", command=lambda: transformation_my(e, e1, e2)).place(x=0, y=150)

            tk.Button(win, text="格式转换", command=transformation, bg="yellow", fg="black").place(x=300, y=350)
            tk.Button(win, text="计算器", command=calculated, bg="yellow", fg="black").place(x=250, y=350)
            tk.Button(win, text="del_file", command=del_my, bg="yellow", fg="black").place(x=450, y=300)

            tk.Button(win, text="open_text", command=open_text, bg="yellow", fg="black").place(x=350, y=300)

            tk.Button(win, text="open_image", command=open_pic, bg="yellow", fg="black").place(x=250, y=300)
            button_my = tk.Button(win, text="WPS", bg="yellow", fg="black", command=text_my)
            button_my.place(x=350, y=250)

            button_docx()
            button_txt()
            pic_h = tk.PhotoImage(file="1.png")
            canvas = tk.Canvas(win, width=750, height=500, bg="yellow")
            button_a(win, "游戏", 250, 200)
            xiti("欢迎使用tk学习机", 250, 100, win)
            button(win, "语文", 250, 150)
            button_s(win, "数学", 300, 150)
            button_h(win, "化学", 350, 150)
            button_cc(win, "补充古诗", 400, 150)
            tk.Button(win, text="制作二维码", bg="yellow", fg="black", command=lambda: make_qr()).place(x=250, y=250)

    btn = tk.Button(enter_w, text='登陆', fg="black", width=7, compound='center',
                    bg="white", command=lambda: panduan(enter_w))
    btn.pack()
    btn.place(x=330, y=270)
    enter_w.mainloop()


def new_window(enter_w):
    window_one = tk.Toplevel(enter_w)
    window_one.geometry('300x400')
    window_one.title('新界面')

    Lab = tk.Label(window_one, text='new window', compound=tk.CENTER)
    Lab.pack()


original_window()
