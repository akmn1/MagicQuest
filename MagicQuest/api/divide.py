import re

def change_wallpaper():
    print("更换壁纸...")

def change_mouse_cursor():
    print("更换鼠标样式...")

def ai_drawing():
    print("AI 绘制...")

# 定义命令模式和相应的处理函数
command_patterns = {
    r"AI": ai_drawing,
    r"绘画": ai_drawing,
    r"壁纸": change_wallpaper,
    r"鼠标": change_mouse_cursor,
}

def process_command(text):
    for pattern, action in command_patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            action()
            return
    print("未识别的命令，请重试。")

# 测试命令
process_command("请帮我更换壁纸")
process_command("我想更换鼠标样式")
process_command("帮我绘画壁纸")
