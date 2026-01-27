# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sap3.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import Icons.icons_rc as icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(727, 566)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"\n"
"border: none;\n"
"background-color: rgb(33,45,51)\n"
"\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.main_container)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"\n"
"background-color: rgba(61,80,95,100);\n"
"border-radius:10px\n"
"\n"
"}\n"
"\n"
"QLabel {\n"
"\n"
"color:rgb(120,157,186);\n"
"background-color:none;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color:none;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.btn_toggle = QPushButton(self.frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/_imgs/menu2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_toggle)


        self.verticalLayout.addWidget(self.frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy1)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.main_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_7 = QFrame(self.main_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:rgb(120,157,186);")

        self.verticalLayout_5.addWidget(self.label_4)

        self.txt_periodo_inicial = QLineEdit(self.frame_8)
        self.txt_periodo_inicial.setObjectName(u"txt_periodo_inicial")
        self.txt_periodo_inicial.setMinimumSize(QSize(0, 27))
        self.txt_periodo_inicial.setFont(font)
        self.txt_periodo_inicial.setStyleSheet(u"\n"
"\n"
"QLineEdit{ \n"
"\n"
"	background-color: rgba(61,80,95,100);\n"
"	border-radius:10px;\n"
"	color:rgb(255,255,255);\n"
"}")
        self.txt_periodo_inicial.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.txt_periodo_inicial)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color:rgb(120,157,186);")

        self.verticalLayout_6.addWidget(self.label_5)

        self.txt_period_final = QLineEdit(self.frame_9)
        self.txt_period_final.setObjectName(u"txt_period_final")
        self.txt_period_final.setMinimumSize(QSize(0, 27))
        self.txt_period_final.setFont(font)
        self.txt_period_final.setStyleSheet(u"\n"
"\n"
"QLineEdit{ \n"
"\n"
"	background-color: rgba(61,80,95,100);\n"
"	border-radius:10px;\n"
"	color:rgb(255,255,255);\n"
"}")
        self.txt_period_final.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.txt_period_final)


        self.horizontalLayout_5.addWidget(self.frame_9)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.tb_razao = QTableWidget(self.main_frame)
        if (self.tb_razao.columnCount() < 17):
            self.tb_razao.setColumnCount(17)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_razao.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        if (self.tb_razao.rowCount() < 10):
            self.tb_razao.setRowCount(10)
        self.tb_razao.setObjectName(u"tb_razao")
        self.tb_razao.setStyleSheet(u"QHeaderView::section{\n"
"\n"
"	background-color:rgba(61,80,95,100);\n"
"	color:rgb(221,221,221);\n"
"}\n"
"\n"
"QTableWidget{\n"
"	color:rgb(221,221,221);\n"
"\n"
"}")
        self.tb_razao.setRowCount(10)

        self.verticalLayout_7.addWidget(self.tb_razao)


        self.verticalLayout.addWidget(self.main_frame)

        self.frame_3 = QFrame(self.main_container)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgb(120,157,186);")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.main_container)

        self.right_frame = QFrame(self.centralwidget)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMaximumSize(QSize(0, 16777215))
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.right_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_logo = QFrame(self.right_frame)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setStyleSheet(u"QFrame {\n"
"\n"
"background-color: rgba(61,80,95,100);\n"
"border-radius:10px\n"
"\n"
"}\n"
"")
        self.frame_logo.setFrameShape(QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_logo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_6 = QFrame(self.frame_logo)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color:none")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color:none")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_2.addWidget(self.frame_logo)

        self.frame_buttons = QFrame(self.right_frame)
        self.frame_buttons.setObjectName(u"frame_buttons")
        sizePolicy1.setHeightForWidth(self.frame_buttons.sizePolicy().hasHeightForWidth())
        self.frame_buttons.setSizePolicy(sizePolicy1)
        self.frame_buttons.setStyleSheet(u"QFrame {\n"
"\n"
"	background-color: rgba(61,80,95,100);\n"
"	border-radius:10px\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgba(33,43,51,100);\n"
"	border-radius:5px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(120,157,186);\n"
"color:rgb(45,45,45)\n"
"}\n"
"\n"
"")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_buttons)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_login = QPushButton(self.frame_buttons)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(120, 28))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_login)

        self.btn_razao = QPushButton(self.frame_buttons)
        self.btn_razao.setObjectName(u"btn_razao")
        self.btn_razao.setMinimumSize(QSize(120, 28))
        self.btn_razao.setFont(font)
        self.btn_razao.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_razao)

        self.btn_excel = QPushButton(self.frame_buttons)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(120, 28))
        self.btn_excel.setFont(font)
        self.btn_excel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_excel)

        self.btn_email = QPushButton(self.frame_buttons)
        self.btn_email.setObjectName(u"btn_email")
        self.btn_email.setMinimumSize(QSize(120, 28))
        self.btn_email.setFont(font)
        self.btn_email.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_email)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_fechar = QPushButton(self.frame_buttons)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setMinimumSize(QSize(120, 28))
        self.btn_fechar.setFont(font)
        self.btn_fechar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_fechar)


        self.verticalLayout_2.addWidget(self.frame_buttons)


        self.horizontalLayout.addWidget(self.right_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/_imgs/analytics_117968.png\"/><span style=\" font-size:18pt; font-weight:700; vertical-align:super;\">--Relat\u00f3rio SAP MB51 ----&gt;</span></p></body></html>", None))
        self.btn_toggle.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Per\u00edodo Inicial</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Per\u00edodo Final</p></body></html>", None))
        ___qtablewidgetitem = self.tb_razao.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem1 = self.tb_razao.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"TipoMovimento", None));
        ___qtablewidgetitem2 = self.tb_razao.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Centro", None));
        ___qtablewidgetitem3 = self.tb_razao.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem4 = self.tb_razao.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"DescricaoMaterial", None));
        ___qtablewidgetitem5 = self.tb_razao.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"TipoAvalia\u00e7\u00e3o", None));
        ___qtablewidgetitem6 = self.tb_razao.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Lote", None));
        ___qtablewidgetitem7 = self.tb_razao.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ElementoPEP", None));
        ___qtablewidgetitem8 = self.tb_razao.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Doc.Material", None));
        ___qtablewidgetitem9 = self.tb_razao.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"DataL\u00e7to.", None));
        ___qtablewidgetitem10 = self.tb_razao.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtablewidgetitem11 = self.tb_razao.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Pedido", None));
        ___qtablewidgetitem12 = self.tb_razao.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Refer\u00eancia", None));
        ___qtablewidgetitem13 = self.tb_razao.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"TextoCabechalo", None));
        ___qtablewidgetitem14 = self.tb_razao.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"DiagramadeRede", None));
        ___qtablewidgetitem15 = self.tb_razao.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"DiagramadeRede", None));
        ___qtablewidgetitem16 = self.tb_razao.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Montante", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por Christian Rufino - 2026", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/_imgs/logo.png\"/></p></body></html>", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_razao.setText(QCoreApplication.translate("MainWindow", u"Raz\u00e3o", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.btn_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.btn_fechar.setText(QCoreApplication.translate("MainWindow", u"Fechar SAP", None))
    # retranslateUi

