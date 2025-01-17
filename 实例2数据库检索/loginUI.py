"""
* 版权所有 (C)2024, YangWenBin
*
* 文件名称：loginUI.py
* 文件标识：无
* 内容摘要：登录界面样式的py文件
* 其它说明：无
* 当前版本：
* 作   者：杨文彬
* 完成日期： 20240606
"""
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(675, 546)
        LoginWindow.setMinimumSize(QtCore.QSize(675, 546))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/个人认证.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(340, 30, 331, 471))
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.closewindowbtn = QtWidgets.QPushButton(self.frame_2)
        self.closewindowbtn.setGeometry(QtCore.QRect(250, 10, 75, 24))
        self.closewindowbtn.setStyleSheet("")
        self.closewindowbtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closewindowbtn.setIcon(icon1)
        self.closewindowbtn.setIconSize(QtCore.QSize(20, 20))
        self.closewindowbtn.setObjectName("closewindowbtn")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 40, 321, 411))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(321, 411))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget_2.setStyleSheet("QLineEdit{\n"
"    border:none;\n"
"    \n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom:1px solid black;\n"
"}\n"
"QPushButton{\n"
"    border-radius:7px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_login)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_account = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_account.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_account.setObjectName("lineEdit_account")
        self.verticalLayout_5.addWidget(self.lineEdit_account)
        self.lineEdit_password = QtWidgets.QLineEdit(self.page_login)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout_5.addWidget(self.lineEdit_password)
        self.pushButton_login_sure = QtWidgets.QPushButton(self.page_login)
        self.pushButton_login_sure.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_login_sure.setBaseSize(QtCore.QSize(0, 35))
        self.pushButton_login_sure.setObjectName("pushButton_login_sure")
        self.verticalLayout_5.addWidget(self.pushButton_login_sure)
        self.stackedWidget_2.addWidget(self.page_login)
        self.page_register = QtWidgets.QWidget()
        self.page_register.setObjectName("page_register")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_register)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_newaccount = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_newaccount.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_newaccount.setObjectName("lineEdit_newaccount")
        self.verticalLayout_6.addWidget(self.lineEdit_newaccount)
        self.lineEdit_newpassword = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_newpassword.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_newpassword.setObjectName("lineEdit_newpassword")
        self.verticalLayout_6.addWidget(self.lineEdit_newpassword)
        self.lineEdit_renewpassword = QtWidgets.QLineEdit(self.page_register)
        self.lineEdit_renewpassword.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_renewpassword.setObjectName("lineEdit_renewpassword")
        self.verticalLayout_6.addWidget(self.lineEdit_renewpassword)
        self.pushButton_register_sure = QtWidgets.QPushButton(self.page_register)
        self.pushButton_register_sure.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_register_sure.setObjectName("pushButton_register_sure")
        self.verticalLayout_6.addWidget(self.pushButton_register_sure)
        self.stackedWidget_2.addWidget(self.page_register)
        self.verticalLayout_4.addWidget(self.stackedWidget_2)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_login = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_login.setStyleSheet("")
        self.pushButton_login.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/登录.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_login.setIcon(icon2)
        self.pushButton_login.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_login.setObjectName("pushButton_login")
        self.horizontalLayout.addWidget(self.pushButton_login)
        self.pushButton_register = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_register.setStyleSheet("")
        self.pushButton_register.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/注册邀请.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_register.setIcon(icon3)
        self.pushButton_register.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_register.setObjectName("pushButton_register")
        self.horizontalLayout.addWidget(self.pushButton_register)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet("font: 700 12pt \"微软雅黑\";\n"
"color: rgb(170, 0, 0);\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5)
        self.stackedWidget.addWidget(self.page_4)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_7 = QtWidgets.QLabel(self.page_6)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_13.addWidget(self.label_7)
        self.stackedWidget.addWidget(self.page_6)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.page_5)
        self.label_6.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_12.addWidget(self.label_6)
        self.stackedWidget.addWidget(self.page_5)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 341, 511))
        self.frame.setMinimumSize(QtCore.QSize(341, 511))
        self.frame.setStyleSheet("#frame{\n"
"    border-image: url(:/icons/空间站.jpg);\n"
"    background-repeat: stretch;\n"
"    border-radius:20px\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(800, 365, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"幼圆\";")
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 24pt \"幼圆\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.verticalLayout_8.addWidget(self.frame_8)
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.closewindowbtn.clicked.connect(LoginWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.lineEdit_account.setPlaceholderText(_translate("LoginWindow", "用户名："))
        self.lineEdit_password.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.pushButton_login_sure.setText(_translate("LoginWindow", "确认"))
        self.lineEdit_newaccount.setPlaceholderText(_translate("LoginWindow", "用户名："))
        self.lineEdit_newpassword.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.lineEdit_renewpassword.setPlaceholderText(_translate("LoginWindow", "确认密码："))
        self.pushButton_register_sure.setText(_translate("LoginWindow", "注册"))
        self.label_3.setText(_translate("LoginWindow", "账号或密码不能为空！"))
        self.label_4.setText(_translate("LoginWindow", "密码错误或用户不存在！"))
        self.label_5.setText(_translate("LoginWindow", "密码不一致！"))
        self.label_7.setText(_translate("LoginWindow", "密码不能为空！"))
        self.label_6.setText(_translate("LoginWindow", "注册成功"))
        self.label.setText(_translate("LoginWindow", "基于PyQt5的"))
        self.label_2.setText(_translate("LoginWindow", "兵器数据库"))
import res_rc
