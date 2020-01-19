#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 都君丨大魔王

import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from people import RandomPeople


class Client(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''窗口绘制'''
        self.setFixedSize(390, 500)
        self.setWindowTitle('请他上台')
        self.setWindowIcon(QtGui.QIcon('./picture/年年有鱼.png'))
        self.client_grid = QGridLayout(self)
        self.label = QLabel('请选择上台人数：')
        self.spin_box = QSpinBox()
        self.spin_box.setValue(3)
        self.create_button = QPushButton('生成(F10)')
        self.create_button.setShortcut('F10')
        self.create_button.clicked.connect(self.create_people_list)
        self.text_browser = QTextBrowser()
        font = QtGui.QFont()
        font.setPointSize(24)
        self.text_browser.setFont(font)
        # 布局
        self.client_grid.addWidget(self.label, 0, 1, 1, 1)
        self.client_grid.addWidget(self.spin_box, 0, 2)
        self.client_grid.addWidget(self.create_button, 0, 3, 1, 1)
        self.client_grid.addWidget(self.text_browser, 1, 1, 1, 4)

    def create_people_list(self):
        people_num = self.spin_box.value()
        self.text_browser.clear()
        self.random_people = RandomPeople(people_num)
        people_list = self.random_people.create_people()
        for people in people_list:
            self.text_browser.append(people)


def main():
    app = QApplication(sys.argv)
    # app.setStyle(QStyleFactory.create('Fusion'))
    client = Client()
    client.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
