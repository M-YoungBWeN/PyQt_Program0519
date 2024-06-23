"""
* 版权所有 (C)2024, YangWenBin
*
* 文件名称：InterfaceUI.py
* 文件标识：无
* 内容摘要：主界面样式的py文件
* 其它说明：无
* 当前版本：
* 作   者：杨文彬
* 完成日期： 20240606
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InterFaceWindow(object):
    def setupUi(self, InterFaceWindow):
        InterFaceWindow.setObjectName("InterFaceWindow")
        InterFaceWindow.resize(768, 494)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/软件开发.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        InterFaceWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(InterFaceWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(768, 474))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(768, 46))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 46))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 141, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/数据库查询.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(170, 0))
        self.frame_4.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom:5px\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_logout = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_logout.setGeometry(QtCore.QRect(0, 10, 75, 24))
        self.pushButton_logout.setStyleSheet("")
        self.pushButton_logout.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/登出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_logout.setIcon(icon2)
        self.pushButton_logout.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 10, 75, 24))
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/最小化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 10, 75, 24))
        self.pushButton_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(750, 418))
        self.frame.setStyleSheet("#frame{\n"
"    border-bottom-left-radius:22px;\n"
"    border-bottom-right-radius:20px;\n"
"    \n"
"    background-color: rgb(244, 244, 244);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("#frame_5{\n"
"    background-color: rgb(13, 85, 157);\n"
"    border-bottom-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"幼圆\";\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:4px\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.pushButton_home = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.pushButton_home.sizePolicy().hasHeightForWidth())
        self.pushButton_home.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/首页白.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_home.setIcon(icon5)
        self.pushButton_home.setIconSize(QtCore.QSize(23, 23))
        self.pushButton_home.setObjectName("pushButton_home")
        self.verticalLayout_28.addWidget(self.pushButton_home)
        self.pushButton_search = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_search.sizePolicy().hasHeightForWidth())
        self.pushButton_search.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/数据库查询白.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search.setIcon(icon6)
        self.pushButton_search.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_search.setObjectName("pushButton_search")
        self.verticalLayout_28.addWidget(self.pushButton_search)
        self.pushButton_db_mange = QtWidgets.QPushButton(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.pushButton_db_mange.sizePolicy().hasHeightForWidth())
        self.pushButton_db_mange.setSizePolicy(sizePolicy)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/数据库管理 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_db_mange.setIcon(icon7)
        self.pushButton_db_mange.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_db_mange.setObjectName("pushButton_db_mange")
        self.verticalLayout_28.addWidget(self.pushButton_db_mange)
        self.frame_16 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_28.addWidget(self.frame_16)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setStyleSheet("#frame_9{\n"
"borer-bottom-left-radius:20px;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_myaccount = QtWidgets.QPushButton(self.frame_9)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/个人信息.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_myaccount.setIcon(icon8)
        self.pushButton_myaccount.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_myaccount.setObjectName("pushButton_myaccount")
        self.verticalLayout_3.addWidget(self.pushButton_myaccount)
        self.pushButton_support = QtWidgets.QPushButton(self.frame_9)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/服务白.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_support.setIcon(icon9)
        self.pushButton_support.setIconSize(QtCore.QSize(18, 18))
        self.pushButton_support.setObjectName("pushButton_support")
        self.verticalLayout_3.addWidget(self.pushButton_support)
        self.pushButton_help = QtWidgets.QPushButton(self.frame_9)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/帮助.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_help.setIcon(icon10)
        self.pushButton_help.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_help.setObjectName("pushButton_help")
        self.verticalLayout_3.addWidget(self.pushButton_help)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("#frame_6{\n"
"    background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius:20px;\n"
"\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget.setStyleSheet("#stackedWidget{\n"
"border-bottom-right-radius:20px;\n"
"background-color: rgb(244, 244, 244);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home_page = QtWidgets.QWidget()
        self.page_home_page.setObjectName("page_home_page")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_home_page)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_11 = QtWidgets.QFrame(self.page_home_page)
        self.frame_11.setStyleSheet("#frame_8{\n"
"\n"
"    \n"
"    background-color: rgb(244, 244, 244);\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setContentsMargins(12, 0, 12, 12)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_6.setStyleSheet("\n"
"border:none;\n"
"font: 20pt \"幼圆\";")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/首页.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon11)
        self.pushButton_6.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_11.addWidget(self.pushButton_6, 0, QtCore.Qt.AlignLeft)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setContentsMargins(20, 0, 20, -1)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_19 = QtWidgets.QFrame(self.frame_13)
        self.frame_19.setStyleSheet("QLabel{\n"
"    \n"
"    font: 700 10pt \"微软雅黑\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"* {\n"
"    outline: none;\n"
"}\n"
"\n"
"QDialog {\n"
"    background: #D6DBE9;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #A0A0A0; /* 边框宽度为1px，颜色为#A0A0A0 */\n"
"    border-radius: 3px; /* 边框圆角 */\n"
"    padding-left: 5px; /* 文本距离左边界有5px */\n"
"    background-color: #F2F2F2; /* 背景颜色 */\n"
"    color: #A0A0A0; /* 文本颜色 */\n"
"    selection-background-color: #A0A0A0; /* 选中文本的背景颜色 */\n"
"    selection-color: #F2F2F2; /* 选中文本的颜色 */\n"
"    font-family: \"Microsoft YaHei\"; /* 文本字体族 */\n"
"    font-size: 10pt; /* 文本字体大小 */\n"
"}\n"
"\n"
"QLineEdit:hover { /* 鼠标悬浮在QLineEdit时的状态 */\n"
"    border: 1px solid #298DFF;\n"
"    border-radius: 3px;\n"
"    background-color: #F2F2F2;\n"
"    color: #298DFF;\n"
"    selection-background-color: #298DFF;\n"
"    selection-color: #F2F2F2;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"] { /* QLineEdit有输入掩码时的状态 */\n"
"    lineedit-password-character: 9679;\n"
"    lineedit-password-mask-delay: 2000;\n"
"}\n"
"\n"
"QLineEdit:disabled { /* QLineEdit在禁用时的状态 */\n"
"    border: 1px solid #CDCDCD;\n"
"    background-color: #CDCDCD;\n"
"    color: #B4B4B4;\n"
"}\n"
"\n"
"QLineEdit:read-only { /* QLineEdit在只读时的状态 */\n"
"    background-color: #CDCDCD;\n"
"    color: #F2F2F2;\n"
"}\n"
"")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_23 = QtWidgets.QFrame(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_23.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_23)
        self.horizontalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.frame_23)
        self.label_12.setMinimumSize(QtCore.QSize(0, 20))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_12.setStyleSheet("font: 12pt \"幼圆\";\n"
"    color: rgb(0, 0, 0);\n"
"")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.verticalLayout_12.addWidget(self.frame_23)
        self.frame_24 = QtWidgets.QFrame(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_24)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_25 = QtWidgets.QFrame(self.frame_24)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label = QtWidgets.QLabel(self.frame_25)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.verticalLayout_14.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.frame_25)
        self.label_7.setMinimumSize(QtCore.QSize(0, 20))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_14.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_25)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_14.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame_25)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_14.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_25)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_14.addWidget(self.label_10)
        self.horizontalLayout_4.addWidget(self.frame_25)
        self.frame_26 = QtWidgets.QFrame(self.frame_24)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.lineEdit_db_name = QtWidgets.QLineEdit(self.frame_26)
        self.lineEdit_db_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_db_name.setCursorPosition(19)
        self.lineEdit_db_name.setDragEnabled(False)
        self.lineEdit_db_name.setClearButtonEnabled(True)
        self.lineEdit_db_name.setObjectName("lineEdit_db_name")
        self.verticalLayout_15.addWidget(self.lineEdit_db_name)
        self.lineEdit_db_user = QtWidgets.QLineEdit(self.frame_26)
        self.lineEdit_db_user.setClearButtonEnabled(True)
        self.lineEdit_db_user.setObjectName("lineEdit_db_user")
        self.verticalLayout_15.addWidget(self.lineEdit_db_user)
        self.lineEdit_db_password = QtWidgets.QLineEdit(self.frame_26)
        self.lineEdit_db_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_db_password.setClearButtonEnabled(True)
        self.lineEdit_db_password.setObjectName("lineEdit_db_password")
        self.verticalLayout_15.addWidget(self.lineEdit_db_password)
        self.lineEdit_db_host = QtWidgets.QLineEdit(self.frame_26)
        self.lineEdit_db_host.setClearButtonEnabled(True)
        self.lineEdit_db_host.setObjectName("lineEdit_db_host")
        self.verticalLayout_15.addWidget(self.lineEdit_db_host)
        self.lineEdit_db_port = QtWidgets.QLineEdit(self.frame_26)
        self.lineEdit_db_port.setClearButtonEnabled(True)
        self.lineEdit_db_port.setObjectName("lineEdit_db_port")
        self.verticalLayout_15.addWidget(self.lineEdit_db_port)
        self.horizontalLayout_4.addWidget(self.frame_26)
        self.verticalLayout_12.addWidget(self.frame_24)
        self.frame_20 = QtWidgets.QFrame(self.frame_19)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_db_change_sure = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_db_change_sure.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_db_change_sure.setStyleSheet("QPushButton{\n"
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
        self.pushButton_db_change_sure.setObjectName("pushButton_db_change_sure")
        self.horizontalLayout_9.addWidget(self.pushButton_db_change_sure)
        self.verticalLayout_12.addWidget(self.frame_20, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_10.addWidget(self.frame_19)
        self.frame_21 = QtWidgets.QFrame(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 67)
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_22 = QtWidgets.QFrame(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_22.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_22)
        self.horizontalLayout_11.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.frame_22)
        self.label_11.setMinimumSize(QtCore.QSize(0, 20))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_11.setStyleSheet("font: 12pt \"幼圆\";\n"
"    color: rgb(0, 0, 0);\n"
"")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.verticalLayout_13.addWidget(self.frame_22)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setStyleSheet("QTextEdit\n"
"{\n"
"border: 1px solid grey;  \n"
"border-radius:3px;\n"
"padding: 1px 18px 1px 3px;  \n"
"font: 75 10pt \"微软雅黑\";\n"
"    background-color: rgb(228, 228, 228);\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_13.addWidget(self.textBrowser)
        self.horizontalLayout_10.addWidget(self.frame_21)
        self.verticalLayout_11.addWidget(self.frame_13)
        self.verticalLayout_10.addWidget(self.frame_11)
        self.stackedWidget.addWidget(self.page_home_page)
        self.page_inquire_page = QtWidgets.QWidget()
        self.page_inquire_page.setObjectName("page_inquire_page")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_inquire_page)
        self.verticalLayout_16.setContentsMargins(12, 0, 12, 12)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_inquire_page)
        self.pushButton_8.setStyleSheet("\n"
"border:none;\n"
"font: 20pt \"幼圆\";")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/数据库查询1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon12)
        self.pushButton_8.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_16.addWidget(self.pushButton_8, 0, QtCore.Qt.AlignLeft)
        self.frame_10 = QtWidgets.QFrame(self.page_inquire_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setMinimumSize(QtCore.QSize(590, 62))
        self.frame_10.setMaximumSize(QtCore.QSize(590, 62))
        self.frame_10.setStyleSheet("\n"
"\n"
"/* 未下拉时，QComboBox的样式 */\n"
"QComboBox {\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    background: transparent; \n"
"    border: 1px solid gray; \n"
"    color: #333333;\n"
"    border-color: #E5E5E5;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"/* 点击QComboBox后的已选中项的样式 */\n"
"QComboBox:on {\n"
"    \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(218, 218, 218);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QLabel{\n"
"    \n"
"    font: 700 10pt \"微软雅黑\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"* {\n"
"    outline: none;\n"
"}\n"
"\n"
"QDialog {\n"
"    background: #D6DBE9;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #A0A0A0; /* 边框宽度为1px，颜色为#A0A0A0 */\n"
"    border-radius: 3px; /* 边框圆角 */\n"
"    padding-left: 5px; /* 文本距离左边界有5px */\n"
"    background-color: #F2F2F2; /* 背景颜色 */\n"
"    color: #A0A0A0; /* 文本颜色 */\n"
"    selection-background-color: #A0A0A0; /* 选中文本的背景颜色 */\n"
"    selection-color: #F2F2F2; /* 选中文本的颜色 */\n"
"    font-family: \"Microsoft YaHei\"; /* 文本字体族 */\n"
"    font-size: 10pt; /* 文本字体大小 */\n"
"}\n"
"\n"
"QLineEdit:hover { /* 鼠标悬浮在QLineEdit时的状态 */\n"
"    border: 1px solid #298DFF;\n"
"    border-radius: 3px;\n"
"    background-color: #F2F2F2;\n"
"    color: #298DFF;\n"
"    selection-background-color: #298DFF;\n"
"    selection-color: #F2F2F2;\n"
"}\n"
"\n"
"QLineEdit[echoMode=\"2\"] { /* QLineEdit有输入掩码时的状态 */\n"
"    lineedit-password-character: 9679;\n"
"    lineedit-password-mask-delay: 2000;\n"
"}\n"
"\n"
"QLineEdit:disabled { /* QLineEdit在禁用时的状态 */\n"
"    border: 1px solid #CDCDCD;\n"
"    background-color: #CDCDCD;\n"
"    color: #B4B4B4;\n"
"}\n"
"\n"
"QLineEdit:read-only { /* QLineEdit在只读时的状态 */\n"
"    background-color: #CDCDCD;\n"
"    color: #F2F2F2;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"    border-radius:9px;\n"
"    background-color: rgb(0, 0, 0);\n"
"\n"
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
"\n"
"padding-left:2px;\n"
"padding-top:1px;\n"
"}\n"
"")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.comboBox_db_select = QtWidgets.QComboBox(self.frame_10)
        self.comboBox_db_select.setGeometry(QtCore.QRect(80, 6, 191, 22))
        self.comboBox_db_select.setObjectName("comboBox_db_select")
        self.comboBox_db_select.addItem("")
        self.comboBox_db_select.addItem("")
        self.comboBox_db_select.addItem("")
        self.comboBox_db_select.addItem("")
        self.label_2 = QtWidgets.QLabel(self.frame_10)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 54, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame_10)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        self.label_5.setGeometry(QtCore.QRect(290, 40, 81, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_input_types_2 = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_input_types_2.setGeometry(QtCore.QRect(370, 40, 131, 20))
        self.lineEdit_input_types_2.setObjectName("lineEdit_input_types_2")
        self.pushButton_select_types_2 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_select_types_2.setGeometry(QtCore.QRect(510, 39, 45, 22))
        self.pushButton_select_types_2.setObjectName("pushButton_select_types_2")
        self.comboBox_db_select_types = QtWidgets.QComboBox(self.frame_10)
        self.comboBox_db_select_types.setGeometry(QtCore.QRect(120, 38, 151, 22))
        self.comboBox_db_select_types.setObjectName("comboBox_db_select_types")
        self.comboBox_db_select_types.addItem("")
        self.verticalLayout_16.addWidget(self.frame_10)
        self.stackedWidget_db_select = QtWidgets.QStackedWidget(self.page_inquire_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.stackedWidget_db_select.sizePolicy().hasHeightForWidth())
        self.stackedWidget_db_select.setSizePolicy(sizePolicy)
        self.stackedWidget_db_select.setStyleSheet("/*QTableView 左上角样式*/\n"
"QTableView QTableCornerButton::section {\n"
"   /*  background: red;\n"
"    border: 2px outset red;*/\n"
"    color: red;\n"
"    background-color: rgb(64, 64, 64);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color: rgb(64, 64, 64);\n"
" }\n"
"\n"
" QTableView {\n"
"    color: white;                                       /*表格内文字颜色*/\n"
"    gridline-color: black;                              /*表格内框颜色*/\n"
"    background-color: rgb(108, 108, 108);               /*表格内背景色*/\n"
"    alternate-background-color: rgb(64, 64, 64);\n"
"    selection-color: white;                             /*选中区域的文字颜色*/\n"
"    selection-background-color: rgb(77, 77, 77);        /*选中区域的背景色*/\n"
"    border: 2px groove gray;\n"
"    border-radius: 0px;\n"
"    padding: 2px 4px;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"    background-color: rgb(108, 108, 108);\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border:0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:0px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color: rgb(64, 64, 64);\n"
"    border: 5px solid #f6f7fa;\n"
"    border-radius:0px;\n"
"    border-color: rgb(64, 64, 64);\n"
"} \n"
"\n"
"\n"
"/*表右侧的滑条*/\n"
"QScrollBar:vertical{\n"
"background:#484848;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-width:12px;\n"
"}\n"
"\n"
"/*滑块*/\n"
"QScrollBar::handle:vertical{\n"
"background:#CCCCCC;\n"
"}\n"
"/*\n"
"滑块悬浮，按下*/\n"
"QScrollBar::handle:hover:vertical,QScrollBar::handle:pressed:vertical{\n"
"background:#A7A7A7;\n"
"}\n"
"/*\n"
"滑块已经划过的区域*/\n"
"QScrollBar::sub-page:vertical{\n"
"background:444444;\n"
"}\n"
"\n"
"/*\n"
"滑块还没有划过的区域*/\n"
"QScrollBar::add-page:vertical{\n"
"background:5B5B5B;\n"
"}\n"
"\n"
"/*页面下移的按钮*/\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"}\n"
"/*页面上移的按钮*/\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}")
        self.stackedWidget_db_select.setObjectName("stackedWidget_db_select")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.tableWidget_select_types_result = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget_select_types_result.setObjectName("tableWidget_select_types_result")
        self.tableWidget_select_types_result.setColumnCount(0)
        self.tableWidget_select_types_result.setRowCount(0)
        self.verticalLayout_27.addWidget(self.tableWidget_select_types_result)
        self.stackedWidget_db_select.addWidget(self.page_4)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget_db_select.addWidget(self.page_2)
        self.page_all_weapons = QtWidgets.QWidget()
        self.page_all_weapons.setObjectName("page_all_weapons")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.page_all_weapons)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.tableWidget_all_weapons = QtWidgets.QTableWidget(self.page_all_weapons)
        self.tableWidget_all_weapons.setObjectName("tableWidget_all_weapons")
        self.tableWidget_all_weapons.setColumnCount(0)
        self.tableWidget_all_weapons.setRowCount(0)
        self.verticalLayout_22.addWidget(self.tableWidget_all_weapons)
        self.stackedWidget_db_select.addWidget(self.page_all_weapons)
        self.page_all_vehicles = QtWidgets.QWidget()
        self.page_all_vehicles.setObjectName("page_all_vehicles")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.page_all_vehicles)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.tableWidget_all_vehicles = QtWidgets.QTableWidget(self.page_all_vehicles)
        self.tableWidget_all_vehicles.setObjectName("tableWidget_all_vehicles")
        self.tableWidget_all_vehicles.setColumnCount(0)
        self.tableWidget_all_vehicles.setRowCount(0)
        self.verticalLayout_23.addWidget(self.tableWidget_all_vehicles)
        self.stackedWidget_db_select.addWidget(self.page_all_vehicles)
        self.page_all_soldiertypes = QtWidgets.QWidget()
        self.page_all_soldiertypes.setObjectName("page_all_soldiertypes")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.page_all_soldiertypes)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.tableWidget_all_soldiertypes = QtWidgets.QTableWidget(self.page_all_soldiertypes)
        self.tableWidget_all_soldiertypes.setObjectName("tableWidget_all_soldiertypes")
        self.tableWidget_all_soldiertypes.setColumnCount(0)
        self.tableWidget_all_soldiertypes.setRowCount(0)
        self.verticalLayout_24.addWidget(self.tableWidget_all_soldiertypes)
        self.stackedWidget_db_select.addWidget(self.page_all_soldiertypes)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.tableWidget_input_2_result = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget_input_2_result.setObjectName("tableWidget_input_2_result")
        self.tableWidget_input_2_result.setColumnCount(0)
        self.tableWidget_input_2_result.setRowCount(0)
        self.verticalLayout_26.addWidget(self.tableWidget_input_2_result)
        self.stackedWidget_db_select.addWidget(self.page_3)
        self.verticalLayout_16.addWidget(self.stackedWidget_db_select)
        self.stackedWidget.addWidget(self.page_inquire_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_18 = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_18)
        self.verticalLayout_20.setContentsMargins(12, 0, 12, 12)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_10.setStyleSheet("\n"
"border:none;\n"
"font: 20pt \"幼圆\";")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/个人信息黑.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon13)
        self.pushButton_10.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_20.addWidget(self.pushButton_10, 0, QtCore.Qt.AlignLeft)
        self.frame_28 = QtWidgets.QFrame(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_25.setContentsMargins(120, -1, 120, 60)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.widget_reset_password_3 = QtWidgets.QWidget(self.frame_28)
        self.widget_reset_password_3.setStyleSheet("QLineEdit{\n"
"    border:none;\n"
"    \n"
"    background-color: rgba(255, 255, 255,0);\n"
"    border-bottom:1px solid black;\n"
"}\n"
"QPushButton{\n"
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
        self.widget_reset_password_3.setObjectName("widget_reset_password_3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.widget_reset_password_3)
        self.verticalLayout_18.setContentsMargins(0, 9, 0, 9)
        self.verticalLayout_18.setSpacing(30)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_3 = QtWidgets.QLabel(self.widget_reset_password_3)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setStyleSheet("font: 12pt \"幼圆\";\n"
"    color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_18.addWidget(self.label_3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_reset_password_3)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_5.setInputMask("")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_18.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_reset_password_3)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_18.addWidget(self.lineEdit_6)
        self.pushButton_change_password_3 = QtWidgets.QPushButton(self.widget_reset_password_3)
        self.pushButton_change_password_3.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_change_password_3.setObjectName("pushButton_change_password_3")
        self.verticalLayout_18.addWidget(self.pushButton_change_password_3)
        self.stackedWidget_show_reset_error_3 = QtWidgets.QStackedWidget(self.widget_reset_password_3)
        self.stackedWidget_show_reset_error_3.setMinimumSize(QtCore.QSize(250, 40))
        self.stackedWidget_show_reset_error_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.stackedWidget_show_reset_error_3.setStyleSheet("font: 700 12pt \"微软雅黑\";\n"
"color: rgb(170, 0, 0);\n"
"")
        self.stackedWidget_show_reset_error_3.setObjectName("stackedWidget_show_reset_error_3")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.stackedWidget_show_reset_error_3.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_19 = QtWidgets.QLabel(self.page_9)
        self.label_19.setGeometry(QtCore.QRect(100, 9, 96, 22))
        self.label_19.setMinimumSize(QtCore.QSize(0, 0))
        self.label_19.setObjectName("label_19")
        self.stackedWidget_show_reset_error_3.addWidget(self.page_9)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.label_20 = QtWidgets.QLabel(self.page_14)
        self.label_20.setGeometry(QtCore.QRect(90, 10, 121, 16))
        self.label_20.setObjectName("label_20")
        self.stackedWidget_show_reset_error_3.addWidget(self.page_14)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.label_21 = QtWidgets.QLabel(self.page_15)
        self.label_21.setGeometry(QtCore.QRect(90, 10, 111, 22))
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setStyleSheet("color: rgb(85, 85, 255);")
        self.label_21.setObjectName("label_21")
        self.stackedWidget_show_reset_error_3.addWidget(self.page_15)
        self.verticalLayout_18.addWidget(self.stackedWidget_show_reset_error_3)
        self.verticalLayout_25.addWidget(self.widget_reset_password_3)
        self.verticalLayout_20.addWidget(self.frame_28)
        self.verticalLayout_19.addWidget(self.frame_18)
        self.stackedWidget.addWidget(self.page)
        self.page_support_page = QtWidgets.QWidget()
        self.page_support_page.setObjectName("page_support_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_support_page)
        self.verticalLayout_6.setContentsMargins(0, 0, 12, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_8 = QtWidgets.QFrame(self.page_support_page)
        self.frame_8.setStyleSheet("#frame_8{\n"
"\n"
"    \n"
"    background-color: rgb(244, 244, 244);\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setContentsMargins(12, 0, 12, 12)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_5.setStyleSheet("\n"
"border:none;\n"
"font: 20pt \"幼圆\";")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/服务.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon14)
        self.pushButton_5.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_5.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignLeft)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("/*QTabWidget*/\n"
"QTabWidget::pane{\n"
"border:none;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"     left: 0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"     \n"
"    background-color: rgb(255, 255, 255);\n"
"     /*border: 2px solid #C4C4C3;*/\n"
"     border-bottom-color: #C2C7CB;\n"
"     min-width: 60px;\n"
"     padding: 2px;\n"
" }\n"
"\n"
"QTabBar::tab:selected{\n"
"    \n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab:!selected{\n"
"    \n"
"    background-color: rgb(230, 230, 230);\n"
"    margin-top:5px;\n"
"}\n"
"/*四个下属界面*/\n"
"#tab,#tab_2,#tab_3,#tab_4{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom-left-radius:20px;\n"
" border-bottom-right-radius:20px;\n"
"border-top-right-radius:20px;\n"
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_8.setContentsMargins(70, 30, 70, 30)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_support_web = QtWidgets.QPushButton(self.tab)
        self.pushButton_support_web.setMinimumSize(QtCore.QSize(0, 70))
        self.pushButton_support_web.setStyleSheet("\n"
"QPushButton{\n"
"    border-radius:9px;\n"
"    background-color: rgb(0, 0, 0);\n"
"    font: 20pt \"幼圆\";\n"
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
"font: 75 20pt \"幼圆\";\n"
"padding-left:2px;\n"
"padding-top:1px;\n"
"}\n"
"")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/跳转.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_support_web.setIcon(icon15)
        self.pushButton_support_web.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_support_web.setObjectName("pushButton_support_web")
        self.verticalLayout_8.addWidget(self.pushButton_support_web)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setContentsMargins(50, 30, 50, 40)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.stackedWidget.addWidget(self.page_support_page)
        self.page_help_page = QtWidgets.QWidget()
        self.page_help_page.setObjectName("page_help_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_help_page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_15 = QtWidgets.QFrame(self.page_help_page)
        self.frame_15.setStyleSheet("#frame_8{\n"
"\n"
"    \n"
"    background-color: rgb(244, 244, 244);\n"
"}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_17.setContentsMargins(12, 0, 12, 12)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_9.setStyleSheet("\n"
"border:none;\n"
"font: 20pt \"幼圆\";")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/帮助黑.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon16)
        self.pushButton_9.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_17.addWidget(self.pushButton_9, 0, QtCore.Qt.AlignLeft)
        self.frame_17 = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_14.setContentsMargins(20, 0, 20, -1)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_17.addWidget(self.frame_17)
        self.verticalLayout_7.addWidget(self.frame_15)
        self.stackedWidget.addWidget(self.page_help_page)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame)
        InterFaceWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(InterFaceWindow)
        self.statusbar.setObjectName("statusbar")
        InterFaceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InterFaceWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_db_select.setCurrentIndex(2)
        self.stackedWidget_show_reset_error_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_4.clicked.connect(InterFaceWindow.close) # type: ignore
        self.pushButton_3.clicked.connect(InterFaceWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(InterFaceWindow)

    def retranslateUi(self, InterFaceWindow):
        _translate = QtCore.QCoreApplication.translate
        InterFaceWindow.setWindowTitle(_translate("InterFaceWindow", "MainWindow"))
        self.pushButton.setText(_translate("InterFaceWindow", "兵器数据库"))
        self.pushButton_home.setText(_translate("InterFaceWindow", "首页"))
        self.pushButton_search.setText(_translate("InterFaceWindow", "查询"))
        self.pushButton_db_mange.setText(_translate("InterFaceWindow", "数据库管理"))
        self.pushButton_myaccount.setText(_translate("InterFaceWindow", "账号管理"))
        self.pushButton_support.setText(_translate("InterFaceWindow", "支持与服务"))
        self.pushButton_help.setText(_translate("InterFaceWindow", "帮助文档"))
        self.pushButton_6.setText(_translate("InterFaceWindow", "首页"))
        self.label_12.setText(_translate("InterFaceWindow", "连接"))
        self.label.setText(_translate("InterFaceWindow", "数据库名"))
        self.label_7.setText(_translate("InterFaceWindow", "用户"))
        self.label_8.setText(_translate("InterFaceWindow", "密码"))
        self.label_9.setText(_translate("InterFaceWindow", "host"))
        self.label_10.setText(_translate("InterFaceWindow", "port"))
        self.lineEdit_db_name.setText(_translate("InterFaceWindow", "pyqt5_test_database"))
        self.lineEdit_db_user.setText(_translate("InterFaceWindow", "postgres"))
        self.lineEdit_db_password.setText(_translate("InterFaceWindow", "174496"))
        self.lineEdit_db_host.setText(_translate("InterFaceWindow", "localhost"))
        self.lineEdit_db_port.setText(_translate("InterFaceWindow", "5432"))
        self.pushButton_db_change_sure.setText(_translate("InterFaceWindow", "确认"))
        self.label_11.setText(_translate("InterFaceWindow", "信息"))
        self.pushButton_8.setText(_translate("InterFaceWindow", "查询"))
        self.comboBox_db_select.setItemText(0, _translate("InterFaceWindow", "请选择"))
        self.comboBox_db_select.setItemText(1, _translate("InterFaceWindow", "武器及其类型"))
        self.comboBox_db_select.setItemText(2, _translate("InterFaceWindow", "载具及其类型"))
        self.comboBox_db_select.setItemText(3, _translate("InterFaceWindow", "兵种及其武器类型"))
        self.label_2.setText(_translate("InterFaceWindow", "类别"))
        self.label_4.setText(_translate("InterFaceWindow", "细分类别"))
        self.label_5.setText(_translate("InterFaceWindow", "模糊查询"))
        self.pushButton_select_types_2.setText(_translate("InterFaceWindow", "查询"))
        self.comboBox_db_select_types.setItemText(0, _translate("InterFaceWindow", "请选择"))
        self.pushButton_10.setText(_translate("InterFaceWindow", "账号管理"))
        self.label_3.setText(_translate("InterFaceWindow", "更改密码"))
        self.lineEdit_5.setPlaceholderText(_translate("InterFaceWindow", "新密码："))
        self.lineEdit_6.setPlaceholderText(_translate("InterFaceWindow", "确认密码："))
        self.pushButton_change_password_3.setText(_translate("InterFaceWindow", "确认"))
        self.label_19.setText(_translate("InterFaceWindow", "密码不一致！"))
        self.label_20.setText(_translate("InterFaceWindow", "密码不能为空！"))
        self.label_21.setText(_translate("InterFaceWindow", "密码修改成功"))
        self.pushButton_5.setText(_translate("InterFaceWindow", "支持与服务"))
        self.pushButton_support_web.setText(_translate("InterFaceWindow", "麻花与千层饼"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("InterFaceWindow", "服务网站"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("InterFaceWindow", "联系"))
        self.pushButton_9.setText(_translate("InterFaceWindow", "帮助文档"))
import res_rc
