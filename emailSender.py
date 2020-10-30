import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    def __init__(self, topic):
        self.topic = topic

    def send(self):
        mail_content = "Chcieliśmy poinformować, że w aktywnym sprincie znajdują się " +self.topic + " nieprzypisane user stories."
        # The mail addresses and password
        sender_address = 'jiratest34@gmail.com'
        sender_pass = 'rpatask123'
        receiver_address = 'Przemyslaw.Gornik@cybercom.com'
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Nieprzypisane zadania w aktywnym sprincie'  # The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Wysłano email')

