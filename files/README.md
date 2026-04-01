# Nick's Cartoon - Python 动画渲染器

一个基于 Python 的简易动画渲染引擎，支持自定义 DSL（领域特定语言）语法，可快速创建和编辑动画效果。

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-red.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-Built--in-orange.svg)

## ✨ 功能特性

- 🎨 **可视化编辑器**：内置代码编辑器，支持实时编辑和预览
- 📝 **自定义 DSL 语法**：简洁易读的动画描述语言
- 🔄 **变量系统**：支持变量定义和表达式计算
- 🔁 **循环结构**：支持 for 循环批量创建对象
- 🎬 **动画效果**：支持矩形、圆形、文本等对象的位移动画
- ⚡ **渲染优化**：可选的 UI 渲染性能优化功能
- 🖼️ **多种类型**：支持矩形、圆形、文本、图片等多种对象类型

## 📋 系统要求

- Python 3.7+
- Windows/Linux/MacOS
- pygame 2.0+
- tkinter (通常随 Python 安装)

## 🚀 快速开始

### 安装依赖

``` bash
pip install pygame
```
### 运行程序
``` bash
python main.py
```
## 📖 使用指南

### 基本语法

#### 1. 设置区块 `[setup]`

```
[setup] 
-bg_color #000000 # 背景颜色 
-time 10 # 动画时长（秒），0 表示无限 
-fps 60 # 帧率
```
#### 2. 变量定义 `[vars]`
```
[vars] -start_x 100 # 整数变量 
-color1 #FF3366 # 颜色变量 
-speed 2.5 # 浮点数变量
```
#### 3. 对象定义 `[object]`

```
[object] -type rect # 对象类型：rect, circle, text 
-start_pos 100 100 # 起始位置 (x, y) 
-end_pos 400 300 # 结束位置 (x, y) 
-start_time 0 # 开始时间（秒） 
-run_time 2 # 运行时长（秒） 
-size 80 80 # 尺寸 
-bg_color #FF0000 # 颜色 
-end_show 1 # 动画结束后是否显示：1 显示，0 不显示
```
#### 4. 文本对象特殊属性
```
[object] 
-type text 
-text "Hello`World" # 文本内容 ("`"会自动转译为空格)
-font Arial # 字体名称 
-size 24 24 # 字体大小 
-is_bold 1 # 是否加粗
```
#### 5. For 循环（批量创建对象）

```
for i in range(5){ 
[object] 
-type rect 
-start_pos start_x i*100+50 
-end_pos 800 i*100+50 
-start_time i*0.5 
-run_time 1.5 
-bg_color color1 
-size 80 80 
}  #注意表达式中不能包含空格
```
### 完整示例1
```render 
[setup] 
-bg_color #0a0a2a 
-time 10 
-fps 60
[vars] 
-start_x 100 
-color1 #FF3366 
-color2 #33FF66 
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
```

### 完整示例2
```render
[setup]
-bg_color #0a0a2a
-time 10
-fps 60

# ========== 第一章：矩形阵列（0-3秒）==========
[object]
-type rect
-start_pos 0 0
-end_pos 960 540
-start_time 0
-run_time 1.5
-bg_color #FF3366
-size 60 60

[object]
-type rect
-start_pos 960 0
-end_pos 480 540
-start_time 0
-run_time 1.5
-bg_color #33FF66
-size 60 60

[object]
-type rect
-start_pos 0 1080
-end_pos 480 540
-start_time 0
-run_time 1.5
-bg_color #FFCC33
-size 60 60

[object]
-type rect
-start_pos 960 1080
-end_pos 960 540
-start_time 0
-run_time 1.5
-bg_color #3399FF
-size 60 60

[object]
-type rect
-start_pos 480 0
-end_pos 480 540
-start_time 0.3
-run_time 1.2
-bg_color #FF33CC
-size 50 50

[object]
-type rect
-start_pos 480 1080
-end_pos 480 540
-start_time 0.3
-run_time 1.2
-bg_color #33FFCC
-size 50 50

# ========== 第二章：圆形爆炸与旋转（3-6秒）==========
[object]
-type circle
-start_pos 480 540
-end_pos 0 0
-start_time 2.5
-run_time 1.5
-bg_color #FF6600
-size 80 80

[object]
-type circle
-start_pos 480 540
-end_pos 960 0
-start_time 2.5
-run_time 1.5
-bg_color #FFCC00
-size 80 80

[object]
-type circle
-start_pos 480 540
-end_pos 0 1080
-start_time 2.5
-run_time 1.5
-bg_color #00FFCC
-size 80 80

[object]
-type circle
-start_pos 480 540
-end_pos 960 1080
-start_time 2.5
-run_time 1.5
-bg_color #CC00FF
-size 80 80

[object]
-type circle
-start_pos 240 270
-end_pos 720 810
-start_time 3.8
-run_time 1.8
-bg_color #FF3399
-size 70 70

[object]
-type circle
-start_pos 720 270
-end_pos 240 810
-start_time 3.8
-run_time 1.8
-bg_color #33FF99
-size 70 70

[object]
-type circle
-start_pos 240 810
-end_pos 720 270
-start_time 4.0
-run_time 1.6
-bg_color #FF9933
-size 70 70

[object]
-type circle
-start_pos 720 810
-end_pos 240 270
-start_time 4.0
-run_time 1.6
-bg_color #3399FF
-size 70 70

# ========== 第三章：文字飞入与律动（6-8.5秒）==========
[object]
-type text
-start_pos -200 540
-end_pos 480 540
-start_time 5.5
-run_time 1.2
-text "READY?"
-font Arial
-is_bold 1
-bg_color #FFFFFF
-size 50 0

[object]
-type text
-start_pos 1160 540
-end_pos 480 540
-start_time 6.2
-run_time 1.0
-text "SET?"
-font Arial
-is_bold 1
-bg_color #FFFF00
-size 50 0

[object]
-type text
-start_pos 480 -200
-end_pos 480 540
-start_time 6.9
-run_time 1.0
-text "GO!"
-font Arial
-is_bold 1
-bg_color #00FF00
-size 80 0

[object]
-type circle
-start_pos 480 540
-end_pos 480 540
-start_time 7.2
-run_time 0.5
-bg_color #00FF00
-size 120 120

[object]
-type circle
-start_pos 480 540
-end_pos 480 540
-start_time 7.5
-run_time 0.3
-bg_color #FFFFFF
-size 60 60

# ========== 第四章：最终标题展示（8.5-10秒）==========
[object]
-type text
-start_pos 0 540
-end_pos 480 540
-start_time 8.3
-run_time 0.8
-text "NICK'S"
-font Arial
-is_bold 1
-bg_color #FF3366
-size 70 0

[object]
-type text
-start_pos 960 540
-end_pos 480 540
-start_time 8.6
-run_time 0.8
-text "CARTOON"
-font Arial
-is_bold 1
-bg_color #33FF66
-size 70 0

[object]
-type circle
-start_pos 480 540
-end_pos 480 540
-start_time 9.2
-run_time 0.3
-bg_color #FFFFFF
-size 150 150

[object]
-type circle
-start_pos 480 540
-end_pos 480 540
-start_time 9.6
-run_time 0.2
-bg_color #000000
-size 10 10

```

### 完整示例3
```render
[setup]
-bg_color #0a0a2a
-time 12
-fps 60

# ========== 第一部分：文字介绍 ==========
# "Welcome to" 从左飞入
[object]
-type text
-start_pos -300 300
-end_pos 300 300
-start_time 0
-run_time 1.2
-text Welcome`to
-font Arial
-is_bold 1
-bg_color #FFFFFF
-size 48 0

# "Nick's" 从右飞入，稍延迟
[object]
-type text
-start_pos 1100 400
-end_pos 480 400
-start_time 0.5
-run_time 1.0
-text "Nick's"
-font Arial
-is_bold 1
-bg_color #FF3366
-size 60 0

# "Cartoon" 从下方飞入
[object]
-type text
-start_pos 480 800
-end_pos 480 500
-start_time 1.2
-run_time 0.8
-text "Cartoon"
-font Arial
-is_bold 1
-bg_color #33FF66
-size 60 0

# "Animation Generator" 缩放出现
[object]
-type text
-start_pos 240 620
-end_pos 240 620
-start_time 2.2
-run_time 0.6
-text "Animation Generator"
-font Arial
-is_bold 0
-bg_color #CCCCCC
-size 32 0

# "Ready?" 闪烁效果（缩放）
[object]
-type text
-start_pos 400 700
-end_pos 400 700
-start_time 3.2
-run_time 0.5
-text "Ready?"
-font Arial
-is_bold 1
-bg_color #FFCC00
-size 50 0

[object]
-type text
-start_pos 400 700
-end_pos 400 700
-start_time 3.8
-run_time 0.4
-text "Ready?"
-font Arial
-is_bold 1
-bg_color #FFCC00
-size 60 0

[object]
-type text
-start_pos 400 700
-end_pos 400 700
-start_time 4.2
-run_time 0.3
-text "Ready?"
-font Arial
-is_bold 1
-bg_color #FFCC00
-size 55 0

# "SET!" 快速飞入
[object]
-type text
-start_pos -200 700
-end_pos 400 700
-start_time 4.8
-run_time 0.4
-text "SET!"
-font Arial
-is_bold 1
-bg_color #00FF00
-size 70 0

# "GO!" 从中心放大
[object]
-type text
-start_pos 480 540
-end_pos 480 540
-start_time 5.3
-run_time 0.4
-text "GO!"
-font Arial
-is_bold 1
-bg_color #FF3366
-size 30 0

[object]
-type text
-start_pos 480 540
-end_pos 480 540
-start_time 5.7
-run_time 0.3
-text "GO!"
-font Arial
-is_bold 1
-bg_color #FF3366
-size 60 0

[object]
-type text
-start_pos 480 540
-end_pos 480 540
-start_time 6.0
-run_time 0.2
-text "GO!"
-font Arial
-is_bold 1
-bg_color #FF3366
-size 80 0

# 爆炸前提示文字消失（黑色矩形覆盖）
[object]
-type rect
-start_pos 0 0
-end_pos 0 0
-start_time 6.3
-run_time 0.1
-bg_color #000000
-size 1000 1100

# ========== 第二部分：爆炸粒子（约1000个，尺寸稍大）==========
# 24 个方向（每15度一个），每个方向 42 个粒子（矩形+圆形混合）
# 方向角度: 0°,15°,30°,45°,60°,75°,90°,105°,120°,135°,150°,165°,180°,195°,210°,225°,240°,255°,270°,285°,300°,315°,330°,345°
# 为简化，每个方向使用 21 个矩形 + 21 个圆形 = 42 个粒子，24×42=1008
# 所有表达式仅使用循环变量 i 和常数

# 定义方向偏移量 (dx, dy) 对（近似方向）
# 方向列表: 角度 -> (dx, dy) 归一化到约 60 长度，实际飞散距离用 i 控制
# 我们直接生成 24 个方向块，每个块包含矩形和圆形循环

# 方向 0° (右)
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480+(i+1)*45 540
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FF3366
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480+(i+1)*55 540
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FF6600
-size 18 18
}

# 方向 15°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480+(i+1)*44 540+(i+1)*12
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FFCC00
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480+(i+1)*54 540+(i+1)*14
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FFFF00
-size 18 18
}

# 方向 30°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480+(i+1)*40 540+(i+1)*23
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #33FF66
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480+(i+1)*49 540+(i+1)*28
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #00FFCC
-size 18 18
}

# 方向 45°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480+(i+1)*36 540+(i+1)*36
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #00CCFF
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480+(i+1)*44 540+(i+1)*44
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #33CCFF
-size 18 18
}

# 方向 60°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480+(i+1)*23 540+(i+1)*40
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FF33CC
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480+(i+1)*28 540+(i+1)*49
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FF66FF
-size 18 18
}

# 方向 75°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480+(i+1)*12 540+(i+1)*44
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #9933FF
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480+(i+1)*14 540+(i+1)*54
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #CC66FF
-size 18 18
}

# 方向 90° (下)
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480 540+(i+1)*45
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FF6600
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480 540+(i+1)*55
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FFAA00
-size 18 18
}

# 方向 105°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480-(i+1)*12 540+(i+1)*44
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #00FF66
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480-(i+1)*14 540+(i+1)*54
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #33FF99
-size 18 18
}

# 方向 120°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480-(i+1)*23 540+(i+1)*40
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FFCC33
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480-(i+1)*28 540+(i+1)*49
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FFDD66
-size 18 18
}

# 方向 135°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480-(i+1)*36 540+(i+1)*36
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #33FFCC
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480-(i+1)*44 540+(i+1)*44
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #66FFEE
-size 18 18
}

# 方向 150°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480-(i+1)*40 540+(i+1)*23
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FF3399
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480-(i+1)*49 540+(i+1)*28
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FF66BB
-size 18 18
}

# 方向 165°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480-(i+1)*44 540+(i+1)*12
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #33FF99
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480-(i+1)*54 540+(i+1)*14
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #66FFCC
-size 18 18
}

# 方向 180° (左)
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480-(i+1)*45 540
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FF3366
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480-(i+1)*55 540
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FF6688
-size 18 18
}

# 方向 195°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480-(i+1)*44 540-(i+1)*12
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #CCFF33
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480-(i+1)*54 540-(i+1)*14
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #DDFF66
-size 18 18
}

# 方向 210°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480-(i+1)*40 540-(i+1)*23
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FFCC66
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480-(i+1)*49 540-(i+1)*28
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FFDD88
-size 18 18
}

# 方向 225°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480-(i+1)*36 540-(i+1)*36
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #33FF66
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480-(i+1)*44 540-(i+1)*44
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #66FF99
-size 18 18
}

# 方向 240°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480-(i+1)*23 540-(i+1)*40
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FF33CC
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480-(i+1)*28 540-(i+1)*49
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FF66EE
-size 18 18
}

# 方向 255°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480-(i+1)*12 540-(i+1)*44
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #33FFCC
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480-(i+1)*14 540-(i+1)*54
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #66FFEE
-size 18 18
}

# 方向 270° (上)
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480 540-(i+1)*45
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FF6600
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480 540-(i+1)*55
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FFAA33
-size 18 18
}

# 方向 285°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480+(i+1)*12 540-(i+1)*44
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #00FF66
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480+(i+1)*14 540-(i+1)*54
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #33FF99
-size 18 18
}

# 方向 300°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480+(i+1)*23 540-(i+1)*40
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FFCC33
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480+(i+1)*28 540-(i+1)*49
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FFDD66
-size 18 18
}

# 方向 315°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480+(i+1)*36 540-(i+1)*36
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #33FF66
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480+(i+1)*44 540-(i+1)*44
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #66FF99
-size 18 18
}

# 方向 330°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480+(i+1)*40 540-(i+1)*23
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #FF3399
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480+(i+1)*49 540-(i+1)*28
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #FF66BB
-size 18 18
}

# 方向 345°
for i in range(21){
[object]
-type rect
-start_pos 480 540
-end_pos 480+(i+1)*44 540-(i+1)*12
-start_time 6.4
-run_time 0.5+i*0.015
-bg_color #33FF99
-size 16 16
}
for i in range(21){
[object]
-type circle
-start_pos 480 540
-end_pos 480+(i+1)*54 540-(i+1)*14
-start_time 6.5
-run_time 0.4+i*0.015
-bg_color #66FFCC
-size 18 18
}

# ========== 结尾闪光 ==========
[object]
-type rect
-start_pos 0 0
-end_pos 0 0
-start_time 10.5
-run_time 0.2
-bg_color #FFFFFF
-size 1000 1100


```
## 🎯 功能说明

### 支持的对象类型

- **rect**: 矩形
- **circle**: 圆形
- **text**: 文本
- **image**: 图片（需指定图片路径）

### 支持的表达式

- 算术运算：`+`, `-`, `*`, `/`
- 变量引用：直接使用已定义的变量名
- 循环变量：在 for 循环中使用 `i`, `j` 等循环变量

### 界面功能

- **新建**: 清空编辑器，创建新文件
- **打开**: 加载 `.render` 格式文件
- **保存**: 保存为 `.render` 格式
- **播放**: 运行动画预览
- **渲染优化**: 启用性能优化模式

## 📁 项目结构
```
rander/ 
├── main.py # 主程序文件 
├── logo.png # 应用图标（可选） 
└── README.md # 项目说明文档
```
## 🛠️ 开发计划

- [ ] 添加更多图形 primitive（三角形、多边形等）
- [ ] 支持渐变颜色
- [ ] 添加声音播放功能
- [ ] 导出为 GIF/视频格式
- [ ] 可视化拖拽编辑器
- [ ] 粒子系统支持
- [ ] 缓动函数支持

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 👨‍💻 作者

**Nick's Studio**

- Version: 1.0.0
- Build Date: 2024

## 🙏 致谢

感谢以下开源项目：

- [Pygame](https://www.pygame.org/) - 游戏开发库
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python GUI 库

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 Issue
- 发送邮件至开发者邮箱

---

**Enjoy creating animations with Nick's Cartoon! 🎬✨**
