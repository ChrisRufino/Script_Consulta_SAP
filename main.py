from PySide6.QtWidgets import QApplication, QMainWindow,QGraphicsDropShadowEffect
from PySide6.QtGui import QColor
import sys
from ui_mai import Ui_MainWindow


show_elements = {
    'frame','frame_8','frame_9','frame_logo'
}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.txt_period_final.setInputMask('**.**.****')
        self.txt_periodo_inicial.setInputMask('**.**.****')

        for x in show_elements:
            effect = QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0,0,0,255))
            getattr(self,x).setGraphicsEffect(effect)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
