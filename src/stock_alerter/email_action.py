import smtplib
from email.mime.text import MIMEText

class EmailAction:
    """Send an email when a rule is matched"""
    from_email="alert@stocks.com"

    def __init__(self,to):
        self.to_email=to

    def execute(self,content):
        messsage = MIMEText(content)
        messsage["Subject"] = "New Stock Alert"
        messsage["From"]="alert@stocks.com"
        messsage["To"]=self.to_email
        smtp = smtplib.SMTP("email.stocks.com")
        try:
            smtp.send_message(messsage)
        finally:
            smtp.quit()


    