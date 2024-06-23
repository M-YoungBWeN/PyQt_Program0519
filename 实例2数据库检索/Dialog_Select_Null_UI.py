"""
* 版权所有 (C)2024, YangWenBin
*
* 文件名称：Dialog_Select_Null_UI.py
* 文件标识：无
* 内容摘要：报错弹窗界面样式的py文件
* 其它说明：无
* 当前版本：
* 作   者：杨文彬
* 完成日期： 20240606
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSelectNull(object):
    def setupUi(self, DialogSelectNull):
        DialogSelectNull.setObjectName("DialogSelectNull")
        DialogSelectNull.resize(300, 150)
        DialogSelectNull.setMinimumSize(QtCore.QSize(300, 150))
        DialogSelectNull.setMaximumSize(QtCore.QSize(300, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/数据库警告.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogSelectNull.setWindowIcon(icon)
        self.vboxlayout = QtWidgets.QVBoxLayout(DialogSelectNull)
        self.vboxlayout.setObjectName("vboxlayout")
        self.frame = QtWidgets.QFrame(DialogSelectNull)
        self.frame.setStyleSheet("QPushButton{\n"
"    border-radius:9px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 12pt \"幼圆\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:\n"
"qlineargradient(spread:pad,x1:0,x2:0, y1:0, y2:1,\n"
"stop: 0 rgba(100,100,100,255),\n"
"stop: 0.495 rgba(0,0,0,255),\n"
"stop: 0.505 rgba(0,0,0,255),\n"
"stop: 1 rgba(100,100,100,255));\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"幼圆\";\n"
"padding-left:2px;\n"
"padding-top:1px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 700 16pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 30, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.vboxlayout.addWidget(self.frame)

        self.retranslateUi(DialogSelectNull)
        self.pushButton_2.clicked.connect(DialogSelectNull.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogSelectNull)

    def retranslateUi(self, DialogSelectNull):
        _translate = QtCore.QCoreApplication.translate
        DialogSelectNull.setWindowTitle(_translate("DialogSelectNull", "错误"))
        self.label.setText(_translate("DialogSelectNull", "查询未返回结果！"))
        self.pushButton_2.setText(_translate("DialogSelectNull", "确认"))
import res_rc
