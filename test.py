# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:49:46 2020

@author: HJP
"""


import sys

from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty, QUrl, QTimer, QDateTime
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

class Foo(QObject):
    textChanged = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self._text = ""

    @pyqtProperty(str, notify=textChanged)
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if self._text == value:
            return
        self._text = value
        self.textChanged.emit()


def update_value():
    obj.text = "values from PyQt5 :-D : {}".format(QDateTime.currentDateTime().toString())

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    obj = Foo()
    timer = QTimer()
    timer.timeout.connect(update_value)
    timer.start(100)
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("obj", obj)
    engine.load(QUrl("main.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    if app is None : 
        app = QGuiApplication(sys.argv)        
    else:
        app = QGuiApplication.instance()        
        
    sys.exit(app.exec_())