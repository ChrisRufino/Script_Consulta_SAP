import win32com.client
import win32clipboard
import pandas as pd


SapGuiAuto = win32com.client.GetObject("SAPGUI")
application = SapGuiAuto.GetScriptingEngine

connection = application.Children(0)
session = connection.Children(0)

session.findById("wnd[0]").maximize()

session.findById("wnd[0]/tbar[0]/okcd").text = "mb51"
session.findById("wnd[0]").sendVKey(0)
session.findById("wnd[0]/usr/radRFLAT_L").setFocus()
session.findById("wnd[0]/usr/radRFLAT_L").select() 
session.findById("wnd[0]/usr/ctxtALV_DEF").text = "/dd3l"
session.findById("wnd[0]/usr/ctxtALV_DEF").setFocus() 
session.findById("wnd[0]/usr/ctxtALV_DEF").caretPosition = 5
session.findById("wnd[0]").sendVKey (0)
session.findById("wnd[0]/usr/ctxtBUDAT-LOW").text = '01.01.2026'
session.findById("wnd[0]/usr/ctxtBUDAT-HIGH").text = '10.01.2026'
session.findById("wnd[0]/usr/ctxtBUDAT-HIGH").setFocus() 
session.findById("wnd[0]/usr/ctxtBUDAT-HIGH").caretPosition = 10
session.findById("wnd[0]").sendVKey(0)
session.findById("wnd[0]/usr/btn%_WERKS_%_APP_%-VALU_PUSH").press() 
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,0]").text = "2096"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,1]").text = "2914"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,2]").text = "2929"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,3]").text = "2944"
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,3]").setFocus() 
session.findById("wnd[1]/usr/tabsTAB_STRIP/tabpSIVA/ssubSCREEN_HEADER:SAPLALDB:3010/tblSAPLALDBSINGLE/ctxtRSCSEL_255-SLOW_I[1,3]").caretPosition = 4
session.findById("wnd[1]").sendVKey (0)
session.findById("wnd[1]/tbar[0]/btn[8]").press() 
session.findById("wnd[0]/tbar[1]/btn[8]").press() 
session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[2]").select() 
session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[4,0]").select() 
session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[4,0]").setFocus()
session.findById("wnd[1]/tbar[0]/btn[0]").press() 
session.findById("wnd[0]/tbar[0]/btn[12]").press() 
session.findById("wnd[0]/tbar[0]/btn[12]").press()

win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

# with open('report.txt','w+') as f:
#   f.write(data)


tratativaData = pd.read_clipboard(sep='|', skiprows= range(0,1), on_bad_lines='skip', encoding='UTF-8')

tratativaData.drop(columns=['Unnamed: 0', 'Unnamed: 19'], inplace=True)


# tratativaData.tail() pegar as ultimas 5 linhas 

tratarColumns = tratativaData.columns = (
    tratativaData.columns
    .str.encode('latin1', errors='ignore')     # remove caracteres bugados
    .str.decode('latin1')                      # volta para string limpa
    .str.strip()                               # remove espaços nas bordas
    .str.replace(r'\s+', ' ', regex=True)      # substitui múltiplos espaços
)

tratativaData.drop(tratativaData.loc[tratativaData['TMv'].str.strip()=='TMv'].index, inplace=True) # remover dados duplicados na linha

tratativaData.dropna(subset=['TMv','Lote'], inplace=True) #eliminar NaN

# tratativaData['DiagRede'] = tratativaData["DiagRede"].apply(lambda x: str(x).strip) # Remover os espaços em branco na coluna, que sao sõ totalizadores

# tratativaData.drop(tratativaData.loc[tratativaData['DiagRede']==''].index, inplace=True)  

tratativaData = tratativaData.drop(tratativaData.index[-1]) # eliminado a ultima linha = totalizador

tratativaData['Montante MI'] = tratativaData["Montante MI"].apply(lambda x: float (x.replace('-',"").replace('.','').replace(",",".")))
print(tratativaData.dtypes)
print(tratativaData.head())
