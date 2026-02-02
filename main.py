from PySide6.QtWidgets import QApplication, QMainWindow,QGraphicsDropShadowEffect,QMessageBox,QTableWidgetItem
from PySide6.QtGui import QColor, QIcon
import sys
from qt_designer.ui_mai import Ui_MainWindow
from PySide6 import QtCore
from Sap.sap import SapGui
import pandas as pd
from datetime import datetime
from functions import Email_report






show_elements = {
    'frame','frame_8','frame_9','frame_logo',"frame_buttons"
}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        appIcon = QIcon(':/icons/_imgs/analytics_117968.png')
        self.setWindowIcon(appIcon)
        self.txt_period_final.setInputMask('00.00.0000;_')
        self.txt_periodo_inicial.setInputMask('00.00.0000;_')

        self.Sap =SapGui()

        #########################################
        #Botões de comando

        self.btn_toggle.clicked.connect(self.right_menu)
        self.btn_fechar.clicked.connect(lambda: self.Sap.close_SAP())
        self.btn_razao.clicked.connect(self.leadger_report)
        self.btn_excel.clicked.connect(self.report_excel)
        self.btn_login.clicked.connect(lambda: self.Sap.sapLogin())
        self.btn_email.clicked.connect(self.send_email)

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
        
        data = self.Sap.leadger(self.txt_periodo_inicial.text(),self.txt_period_final.text()) #pega as datas adicionadas no executavel
        data = data.values.tolist() # transforma os dados em lista

        self.tb_razao.setRowCount(len(data)) # conta as linhas na tabela

        for row, text in enumerate(data):
            for column, data in enumerate(text):
                self.tb_razao.setItem(row,column,QTableWidgetItem(str(data)))

    def report_excel(self):
        try:
            # Verificar se há dados
            if self.tb_razao.rowCount() == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Aviso")
                msg.setText("Não há dados na tabela para exportar!")
                msg.exec()
                return
            
            # Coletar dados da tabela
            update_data = []
            for row in range(self.tb_razao.rowCount()):
                row_data = []
                for column in range(self.tb_razao.columnCount()):
                    item = self.tb_razao.item(row, column)
                    row_data.append(item.text() if item else "")
                update_data.append(row_data)
            
            # Criar DataFrame - 
            self.df = pd.DataFrame(update_data, columns=[
                'Usuário', 'TipoMovimento', 'Centro', 'Depósito', 'Material',
                'Descrição', 'TipoAv.', 'Lote', 'ElementoPep', 'Doc.Material',
                'DataLancamento', 'Quantidade', 'Pedido', 'Referencia',
                'TextoCabecalho', 'Reserva', 'DiagramaRede', 'Montante'
            ])
            
            # CONVERTER MONTANTE(remove . e troca , por .)
            # self.df['Montante'] = pd.to_numeric(
            #     self.df['Montante'].astype(str)
            #     .str.replace('.', '', regex=False)      # Remove separador de milhar
            #     .str.replace(',', '.', regex=False)     # Troca vírgula por ponto
            #     .str.replace('-', '', regex=False)      # Remove hífen
            #     .str.strip(),                            # Remove espaços
            #     errors='coerce'                          # Converte erros para NaN
            # ).fillna(0.0)                                # Substitui NaN por 0
            
            self.df['Montante'] = self.df['Montante'].astype(float)
            # Agrupar valores
            self.total = self.df.groupby("Material")['Montante'].sum().reset_index()
            
            filename = f"MB51_{datetime.now().strftime('%d-%m-%Y')}.xlsx"
            # SALVAR NO EXCEL - 
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                self.total.to_excel(writer, sheet_name="Valor_Material_Movimentado", index=False)
                self.df.to_excel(writer, sheet_name='MB51', index=False)
            
            # Mensagem de sucesso
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Sucesso")
            msg.setText(f"Relatório exportado com sucesso!\nArquivo: {filename}")
            msg.exec()
        
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText(f"Erro ao gerar relatório:\n{str(e)}")
            msg.exec()
            print(f"Erro detalhado: {e}")

    def send_email(self):
        self.report_excel()
        body = f"""
            <h2>Relatório diário SAP</h2> <br>
            <p>Segue relatório da MB51 dos centros: ["2096","2914","2929","2944","2933","2032","20AI","29AF"]</p>
            <p>Valores do montante por material:</p>
            {self.total.to_html()}
            """
        
        e = Email_report()
        e.recipient("christisael@gmail.com",'relatório da MB51')
        e.email_body(body)
        filename = f"MB51_{datetime.now().strftime('%d-%m-%Y')}.xlsx"
        e.email_attachment(f'C:/Users/BZZL/Downloads/meusproejtos/Script_Consulta_SAP/{filename}')
        e.email_send()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Email")
        msg.setText("Email enviado")
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
