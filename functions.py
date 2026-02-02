import win32com.client as win32

class Email_report():
  def __init__(self) -> None:
    self.outlook= win32.Dispatch("outlook.application")
    self.email = self.outlook.CreateItem(0)

  
  def recipient(self, para, assunto):
    self.email.To = para
    self.email.Subject = assunto

  
  def email_body(self, body):
    self.email.HTMLbody = body

  def email_attachment(self, anexo):
     self.email.Attachments.Add(anexo) 

  def email_send(self):
    self.email.Send()