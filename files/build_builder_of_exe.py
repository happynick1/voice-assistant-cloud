"""
main_system.py 的 cx_Freeze 打包配置
优化目标：最小化 EXE 文件大小
"""
import sys
from cx_Freeze import setup, Executable
import os
import shutil

# 检查文件是否存在并添加到 include_files
include_files = []

# 必须包含的目录
if os.path.exists("builtin_functions"):
    include_files.append(("builtin_functions/", "builtin_functions/"))
if os.path.exists("E:\\语音助手"):
    include_files.append(("E:\\语音助手\\", "E:\\语音助手\\"))
if os.path.exists("插件库"):
    include_files.append(("插件库/", "插件库/"))

# 可选的配置文件和图标
for file in ["logo.ico", "main_system.txt", "tools.py", "插件市场.py"]:
    if os.path.exists(file):
        include_files.append((file, file))

# 依赖项分析 - 排除不必要的模块
build_exe_options = {
    # 排除不需要的模块（减小体积）
    "excludes": [
        "tkinter.test",
        "test",
        "unittest",
        "pydoc",
        "doctest",
        "pdb",
        "email",
        "http",
        "xml",
        "pyshine",
        "cv2",
        "pygame",
        "scipy",
        "pandas",
        "nose",
        "sphinx",
        "IPython",
        "notebook",
        "jupyter",
        "flask",
        "django",
    ],
    
    # 包含必要的文件（只包含存在的文件）
    "include_files": include_files,
    
    # 优化选项
    "optimize": 2,  # 最高级别字节码优化
    "build_exe": "dist/main_system_build",  # 输出目录
    
    # 压缩选项
    "zip_include_packages": ["*"],  # 所有包都压缩到 zip
    "zip_exclude_packages": [],  # 不排除任何包
    
    # 静默模式（减少输出）
    "silent": True,
}

# Windows GUI 应用配置 - 修复新版 cx_Freeze 兼容性
if sys.platform == "win32":
    base = "gui"
else:
    base = None

executables = [
    Executable(
        script="main_system.py",
        base=base,
        target_name="main_system.exe",
        icon="logo.ico" if os.path.exists("logo.ico") else None,
    )
]

setup(
    name="PythonAIAssistant",
    version="5.1.7",
    description="Python AI Assistant Application",
    author="HappyStudio",
    options={"build_exe": build_exe_options},
    executables=executables,
)
