import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QListView, QTableView, QSplitter, QFileSystemModel, \
    QDirModel
# 注意与C++ qt 的区别

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 在新版的C++ Qt里，QDirModel已经被废弃了，可以改为使用QFileSystemModel, PyQt5里目前还能用QDirModel
    model = QDirModel()
    # model = QFileSystemModel()
    # model.setRootPath(QDir.currentPath())

    # 创建三个视图
    tree_view = QTreeView()
    # list_view = QListView()
    # table_view = QTableView()

    # 为视图设置数据模型
    tree_view.setModel(model)
    # list_view.setModel(model)
    # table_view.setModel(model)

    # 将list_view和table_view的选择模型设置为何tree_view相同
    # list_view.setSelectionModel(tree_view.selectionModel())
    # table_view.setSelectionModel(tree_view.selectionModel())

    # 设置信号和槽, 以便使list view 和table view能够随tree view中的点击而变化
    # 当双击tree_view对象中的某个目录时，list_view和table_view对象中也同步显示此选定目录下的所有文件和目录
    # tree_view.doubleClicked.connect(list_view.setRootIndex)
    # tree_view.doubleClicked.connect(table_view.setRootIndex)

    # 将三个视图添加到分裂器中
    splitter = QSplitter()
    splitter.addWidget(tree_view)
    # splitter.addWidget(list_view)
    # splitter.addWidget(table_view)

    # 设置窗口的title
    splitter.setWindowTitle('Model/View example')
    splitter.show()

    sys.exit(app.exec_())

