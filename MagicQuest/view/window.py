import sys
import os
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QStackedWidget, QListWidget, \
    QListWidgetItem, QLabel, QHBoxLayout, QLineEdit, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from lib import common_server
from core import background, cursor, quick_methods, sound_device

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MagicQuest")
        self.setGeometry(100, 100, 600, 400)
        self.temp_var = None #储存键值
        self.image_path = None #储存壁纸的地址
        self.input_value = None  # 初始化用于存储输入框内容的变量
        self.initUI()
        self.is_updating_list = False  # 新增标志位
    def initUI(self):
        self.stack = QStackedWidget(self)
        self.buttons = [QPushButton("鼠标变形咒"), QPushButton("壁纸旅行魔法"),QPushButton("召唤画布精灵"),QPushButton("远古图书馆")]
        for i, button in enumerate(self.buttons):
            button.clicked.connect(lambda _, b=i: self.switch_to_widget(b))

        self.widgets = [QWidget() for _ in range(4)]
        self.setup_first_widget()
        self.setup_second_widget()  # 设置界面二
        self.setup_third_widget()  # 设置界面三
        self.setup_fourth_widget()  # 设置界面三
        for i in range(2, 4):
            layout = QVBoxLayout()
            layout.addWidget(QPushButton(f"这是界面 {i + 1} 的内容"))
            self.widgets[i].setLayout(layout)
            self.stack.addWidget(self.widgets[i])

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        for button in self.buttons:
            layout.addWidget(button)
        layout.addWidget(self.stack)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

################################# 界面一和二 共用列表函数(反正不会同时存在哈啊啊啊)########
    def setup_first_widget(self):
        layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.SingleSelection)
        self.list_widget.itemSelectionChanged.connect(self.on_item_selection_changed)

        layout.addWidget(self.list_widget)

        self.button1 = QPushButton("确定")
        self.button2 = QPushButton("恢复默认设置")
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.button1.clicked.connect(self.on_click_button1)#触发函数触发更换注册表地址
        self.button1.clicked.connect(self.on_click_messBox)  # 提示更新成功
        self.button2.clicked.connect(self.on_click_button2)#点击触发函数触发re_cursor()
        self.button2.clicked.connect(self.on_click_messBox2) #提示回复成功



        self.widgets[0].setLayout(layout)
        self.stack.addWidget(self.widgets[0])
        self.load_data(common_server.file_look(fr"{PROJECT_ROOT}/DB/cursor_resources"),0)
    def setup_second_widget(self):
        layout = QHBoxLayout()  # 使用水平布局
        self.list_widget2 = QListWidget()
        self.list_widget2.setSelectionMode(QListWidget.SingleSelection)
        self.list_widget2.itemSelectionChanged.connect(self.on_item_selection_changed2)
        self.image_label = QLabel()  # 图片显示标签

        layout.addWidget(self.list_widget2, 1)  # 列表占1/3
        layout.addWidget(self.image_label, 2)  # 图片占2/3
        self.button3 = QPushButton("应用")
        self.button3.clicked.connect(self.on_click_button3)#点击触发函数触发壁纸更换
        layout.addWidget(self.button3)
        self.widgets[1].setLayout(layout)
        self.stack.addWidget(self.widgets[1])
        self.load_data(common_server.file_look(fr"{PROJECT_ROOT}/DB/background_resources"),1)


    def on_item_selection_changed(self):#这是用来配置界面一的列表的函数!!
        if not self.is_updating_list:  # 检查标志位状态
            self.is_updating_list = True  # 设置标志位
            try:
                selected_items = self.list_widget.selectedItems()
                if selected_items:
                    item = selected_items[0]
                    self.temp_var = item.data(Qt.UserRole)  # 存储选中项的键值
                    print(item.data(Qt.UserRole))
                    for i in range(self.list_widget.count()):
                        self.list_widget.item(i).setBackground(QColor("white"))  # 重置所有行的背景色
                    item.setBackground(QColor("lightblue"))  # 设置选中项的背景色
            finally:
                self.is_updating_list = False  # 重置标志位
    def on_item_selection_changed2(self):#界面二的列表函数
        selected_items = self.list_widget2.selectedItems()
        if selected_items:
            self.image_path = selected_items[0].data(Qt.UserRole)
            pixmap = QPixmap(self.image_path)
            self.image_label.setPixmap(pixmap.scaled(400, 300, Qt.KeepAspectRatio))

    def load_data(self, data_dict, widget_index):#更新图片地址(界面二的壁纸路径/绝对路径)
        if widget_index == 0:
            list_widget = self.list_widget#切换到列表一
        else:
            list_widget = self.list_widget2#切换到列表二

        list_widget.clear()
        for key, value in data_dict.items():
            list_item = QListWidgetItem(key)
            list_item.setData(Qt.UserRole, value)
            list_widget.addItem(list_item)

    def switch_to_widget(self, index): #切换界面!!!!
        self.stack.setCurrentIndex(index)


    # 弹出提示框函数 不是很好用哦
    def on_click_messBox(self):#弹出提示框函数 不是很好用哦
        messBox = QMessageBox()
        messBox.setWindowTitle(u'提示')
        messBox.setText(u'鼠标样式已更换')
        messBox.exec_()
    def on_click_messBox2(self):#弹出提示框函数 不是很好用哦
        messBox = QMessageBox()
        messBox.setWindowTitle(u'提示')
        messBox.setText(u'鼠标样式已恢复默认')
        messBox.exec_()
  ###################下面是界面一二的三个按钮的点击触发函数##################


    def on_click_button1(self):
        cursor.apply_cursor(self.temp_var)

    def on_click_button2(self):
        cursor.re_cursor()

    def on_click_button3(self):
        background.set_desktop_background(self.image_path)

#############################下面的代码构建界面三  ################################################

    def setup_third_widget(self):
        layout = QVBoxLayout()
        self.image_label3 = QLabel()  # 图片显示区域
        self.image_label3.setFixedSize(400, 300)  # 没法居中?

        # 图片预览区占上3/4
        layout.addWidget(self.image_label3, 3)

        # 文本输入框和按钮占下1/4
        self.text_input = QLineEdit()  # 文本输入框
        self.text_input.setPlaceholderText('输入图片描述,尽量使用英文,用逗号隔开每个元素,例如:gril,blue eyes')  # 设置占位提示字符
        self.update_button = QPushButton("保存文本")
        self.update_button.clicked.connect(self.save_input_content)#点击按钮上传文字

        # 输入框和按钮的布局
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.text_input)
        bottom_layout.addWidget(self.update_button)
        layout.addLayout(bottom_layout, 1)

        self.widgets[2].setLayout(layout)
        self.stack.addWidget(self.widgets[2])

    def save_input_content(self):
        self.input_value = self.text_input.text()  # 保存输入框的内容到变量
        print(f"保存的文本:{self.input_value}")

    def update_image(self, image_path):
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print("加载图片失败，请检查路径:", image_path)
        else:
            self.image_label3.setPixmap(pixmap.scaled(400, 300, Qt.KeepAspectRatio))  # 更新图片

##################################下面的代码构建界面四 以及一些事件槽 ######################################

    def setup_fourth_widget(self):
        layout = QVBoxLayout()

        # 上传鼠标资源按钮和提示
        self.upload_mouse_button = QPushButton("上传鼠标资源")
        self.upload_mouse_button.clicked.connect(self.upload_mouse_resource)
        layout.addWidget(self.upload_mouse_button)
        layout.addWidget(QLabel("请上传鼠标资源文件"))

        # 上传壁纸资源按钮和提示
        self.upload_wallpaper_button = QPushButton("上传壁纸资源")
        self.upload_wallpaper_button.clicked.connect(self.upload_wallpaper_resource)
        layout.addWidget(self.upload_wallpaper_button)
        layout.addWidget(QLabel("请上传壁纸资源文件"))

        # 查看快捷语音按钮和提示
        self.view_shortcut_button = QPushButton("查看快捷语音")
        self.view_shortcut_button.clicked.connect(self.view_shortcut_phrases)
        layout.addWidget(self.view_shortcut_button)
        layout.addWidget(QLabel("查看可用的快捷语音列表"))

        self.widgets[3].setLayout(layout)
        self.stack.addWidget(self.widgets[3])

    def upload_mouse_resource(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择鼠标资源文件", "", "All Files (*)")
        if file_path:
            print("选择的鼠标资源文件路径:", file_path)
            self.call_backend_function(file_path,

                                       "mouse")

    def upload_wallpaper_resource(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择壁纸资源文件", "", "All Files (*)")
        if file_path:
            print("选择的壁纸资源文件路径:", file_path)
            self.call_backend_function(file_path, "wallpaper")

    def view_shortcut_phrases(self):
        messages = ["快捷语音1: 欢迎光临", "快捷语音2: 你好", "快捷语音3: 再见"]
        QMessageBox.information(self, "快捷语音列表", "\n".join(messages))

    def call_backend_function(self, file_path, resource_type):
        # 在这里调用后端函数，并传递文件路径
        print(f"调用后端函数，类型: {resource_type}, 路径: {file_path}")

    def switch_to_widget(self, index):
        self.stack.setCurrentIndex(index)




###################################下面是监听函数!!!!Qt5真是太好用辣!!#############################################

    def keyPressEvent(self, event):##这这这么好用???????无需调用,只要按下,自动调用,全程自动监听?
        if event.key() == Qt.Key_F5:
            self.trigger_function()  # 监听完毕,执行焦土作战doge
        else:
            super().keyPressEvent(event)  # 调用基类方法，处理其他按键事件

    def trigger_function(self):#监听完毕!!立即执行!!!
        print("F5键被按下了，触发功能！")
        # 例如，假设我们要更新图片显示
        self.update_image("E:\MagicQuest\MagicQuest\DB\骑着扫帚的魔法少女.png")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
