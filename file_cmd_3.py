#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
   
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
	self.setWindowTitle('Icon')
	self.setWindowIcon(QIcon('web.png'))

if __name__ == '__min__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
