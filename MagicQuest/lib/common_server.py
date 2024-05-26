# 这个模块包含一些经常被调用的方法和装饰器
import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def file_look(folder_path):
    mylist = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        mylist.setdefault(filename,file_path)
    return mylist
    print(mylist)

folder_path=fr"{PROJECT_ROOT}/DB/cursor_resources"
file_look(folder_path)