from PySide6.QtWidgets import QApplication, QMainWindow,QGraphicsDropShadowEffect,QMessageBox,QTableWidgetItem
from PySide6.QtGui import QColor
import sys
from qt_designer.ui_mai import Ui_MainWindow
from PySide6 import QtCore
from Sap.sap import SapGui

show_elements = {
    'frame','frame_8','frame_9','frame_logo',"frame_buttons"
}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.txt_period_final.setInputMask('00.00.0000;_')
        self.txt_periodo_inicial.setInputMask('00.00.0000;_')

        self.Sap =SapGui()

        #########################################
        #Botões de comando

        self.btn_toggle.clicked.connect(self.right_menu)
        self.btn_fechar.clicked.connect(lambda: self.Sap.close_SAP())
        self.btn_razao.clicked.connect(self.leadger_report)

        ########################################

        for x in show_elements:
            effect = QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0,0,0,255))
            getattr(self,x).setGraphicsEffect(effect)


    def right_menu(self):
        width = self.right_frame.width()

        if width == 0:
            new_width= 200
        else:
            new_width = 0

        self.animation = QtCore.QPropertyAnimation(self.right_frame,b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def leadger_report(self):
        if self.txt_periodo_inicial.text() == ".." or self.txt_period_final.text()=="..":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical) 
            msg.setWindowTitle("Erro")
            msg.setText("Preencher periodo inicial e final")
            msg.exec_()
            
            return






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
