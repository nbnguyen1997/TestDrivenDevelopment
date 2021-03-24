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

class MessageMatcher:
    def __init__(self,expected) :
        self.expected = expected

    def __eq__(self, other):
        return self.expected["Subject"] == other["Subject"] and \
            self.expected["From"] == other["From"] and \
            self.expected["To"] == other["To"] and \
            self.expected["Message"] == other["Message"]
    