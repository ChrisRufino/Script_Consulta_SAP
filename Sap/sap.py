import win32com.client
import subprocess
import pandas as pd
import time
import getpass
from tkinter import simpledialog, Tk
import sys

class SapGui():

  def open_sap(self):
     path = r"C:\Program Files\SAP\FrontEnd\SAPGUI\saplogon.exe"
     subprocess.Popen(path)

  def connect_sap(self):
      SapGuiAuto = win32com.client.GetObject("SAPGUI")
      application = SapGuiAuto.GetScriptingEngine
      self.connection = application.Children(0)
      self.session = self.connection.Children(0)
      self.session.findById("wnd[0]").maximize()
  
  def sapLogin(self):
      self.open_sap()
      time.sleep(3)

      SapGuiAuto = win32com.client.GetObject("SAPGUI")

      if not type(SapGuiAuto) == win32com.client.Dispatch: # se o sap nao for despachado
          return
      application = SapGuiAuto.GetScriptingEngine
      self.connection = application.OpenConnection("SAPSCRIPT",True)
      # self.connection = application.OpenConnection("py4all",True)
      # self.connection = application.OpenConnection("PEP",True)
      time.sleep(3)
      self.session = self.connection.Children(0)

      

      try:
         
      # Pega usuário do Windows
         username = getpass.getuser()

      # Pede senha via janelinha (opcional)
         root = Tk()
         root.withdraw()
         password = simpledialog.askstring("Senha SAP", f"Digite a senha do usuário SAP ({username}):", show='*')
          
         self.session.findById("wnd[0]/usr/txtRSYST-MANDT").text = '800'
         
      #    #usuario
         self.session.findById("wnd[0]/usr/txtRSYST-BNAME").text = username

      #    #senha
         self.session.findById("wnd[0]/usr/pwdRYST-BCODE").text = password

      #    #idioma
         self.session.findById("wnd[0]/usr/txtRSYST-LANGU").text = 'PT'

      #    #Enter
         self.session.findById("wnd[0]").sendVKey(0)

      except:
         print(sys.exc_infor()[0])

  def leadger(self, date_initial, date_finaly):
      self.connect_sap()
      self.session.findById("wnd[0]/tbar[0]/okcd").text = "/nmb51"
      self.session.findById("wnd[0]").sendVKey(0)
      self.session.findById("wnd[0]/usr/ctxtMATNR-LOW").text = ""
      self.session.findById("wnd[0]/usr/ctxtWERKS-LOW").text = ""
      self.session.findById("wnd[0]/usr/ctxtLGORT-LOW").text = ""
      self.session.findById("wnd[0]/usr/ctxtBUDAT-LOW").text = ""
      self.session.findById("wnd[0]/usr/ctxtBUDAT-HIGH").text = ""

      self.session.findById("wnd[0]/usr/radRFLAT_L").setFocus()
      self.session.findById("wnd[0]/usr/radRFLAT_L").select() 
      self.session.findById("wnd[0]/usr/ctxtALV_DEF").text = "/dd3l"
      self.session.findById("wnd[0]/usr/ctxtALV_DEF").setFocus() 
      self.session.findById("wnd[0]/usr/ctxtALV_DEF").caretPosition = 5
      self.session.findById("wnd[0]").sendVKey (0)
      self.session.findById("wnd[0]/usr/ctxtBUDAT-LOW").text = date_initial
      self.session.findById("wnd[0]/usr/ctxtBUDAT-HIGH").text = date_finaly
      self.session.findById("wnd[0]/usr/ctxtBUDAT-HIGH").setFocus() 
      self.session.findById("wnd[0]/usr/ctxtBUDAT-HIGH").caretPosition = 10
      self.session.findById("wnd[0]").sendVKey(0)
      self.session.findById("wnd[0]/usr/btn%_WERKS_%_APP_%-VALU_PUSH").press() 
      self.session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = "2096"
      self.session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,1]").text = "2914"
      self.session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").text = "2929"
      self.session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,3]").text = "2944"
      self.session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,3]").setFocus() 
      self.session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,3]").caretPosition = 4
      self.session.findById("wnd[1]").sendVKey (0)
      self.session.findById("wnd[1]/tbar[0]/btn[8]").press() 
      self.session.findById("wnd[0]/tbar[1]/btn[8]").press() 
      self.session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[2]").select() 
      self.session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[4,0]").select() 
      self.session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[4,0]").setFocus()
      self.session.findById("wnd[1]/tbar[0]/btn[0]").press() 
      self.session.findById("wnd[0]/tbar[0]/btn[12]").press() 
      self.session.findById("wnd[0]/tbar[0]/btn[12]").press()
            
      #faz a leitura do clipboard em um dataframe
      tratativaData = pd.read_clipboard(sep='|', skiprows= range(0,1), on_bad_lines='skip', encoding='UTF-8')

      #tira os espaços da coluna
      tratarColumns = tratativaData.columns = (
      tratativaData.columns
      .str.encode('latin1', errors='ignore')     # remove caracteres bugados
      .str.decode('latin1')                      # volta para string limpa
      .str.strip()                               # remove espaços nas bordas
      .str.replace(r'\s+', ' ', regex=True)      # substitui múltiplos espaços
      )
         #elimina as colunas desnecessárias
      tratativaData.drop(columns=['Unnamed: 0', 'Unnamed: 19'], inplace=True)
      #Retira os espaços em branco no campo TMv
      tratativaData.drop(tratativaData.loc[tratativaData['TMv'].str.strip()=='TMv'].index, inplace=True) # remover dados duplicados na linha
      #Exclui os valores NaN (Not a number) nas colunas TMv e Lote
      tratativaData.dropna(subset=['TMv','Lote'], inplace=True) #eliminar NaN
      # eliminado a ultima linha = totalizador
      tratativaData = tratativaData.drop(tratativaData.index[-1]) 
      #transformando os valores em float para valor americano

      tratativaData['Montante em MI'] = tratativaData["Montante em MI"].apply(lambda x: float (x.replace('-',"").replace('.','').replace(",","."))) 

      tratativaData['DiagRede'] = tratativaData["DiagRede"].apply(lambda x: str(x).strip())
      return tratativaData
  
  def close_SAP(self):
      self.connect_sap()
      self.connection.CloseSession('ses[0]')







