import smtplib
import const_file.MAIL as MAIL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send():
    # Email account details
    sender_email = MAIL.SENDER_EMAIL
    sender_password = MAIL.SENDER_PWD
    recipient_email = [MAIL.RECIPIENT0_EMAIL, MAIL.RECIPIENT1_EMAIL]
    filename = [MAIL.FILE_NAME0, MAIL.FILE_NAME1]

    # Create a message object
    msg = MIMEMultipart()

    # Set the email subject, body, and recipient
    msg['Subject'] = MAIL.SUBJECT
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipient_email)
    body = MAIL.BODY

    # Attach the Excel file to the email
    for file in filename:
        with open(file, 'rb') as attachment:
            part = MIMEApplication(attachment.read(), Name=file)
            part['Content-Disposition'] = f'attachment; filename="{file}"'
            msg.attach(part)


    # Add the email body to the message
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)
    smtp_server.sendmail(sender_email, recipient_email, msg.as_string())
    smtp_server.quit()
