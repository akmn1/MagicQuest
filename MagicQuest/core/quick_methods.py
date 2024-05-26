# 这个模块主要包含了那些锦上添花的快捷方法比如电脑关机和重启
import os


def shutdown_computer():#关机函数
    print("电脑将在10秒后关机... ")
    os.system("shutdown /s /t 10")

def restart_computer():#重启函数
    print("电脑将在10秒后重启... ")
    os.system("shutdown /r /t 10")

