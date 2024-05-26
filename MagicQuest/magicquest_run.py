import os
from view import views
from view import mouse
# 设置项目根目录为全局变量
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if __name__ == "__main__":
    # sound_device.record_audio()
    views.view()