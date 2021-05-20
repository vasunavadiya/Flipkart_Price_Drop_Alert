import smtplib
from email.message import EmailMessage

def alert_system(product, link):
    email_id = 'youremail'
    email_pass = 'email password'

    msg = EmailMessage()
    msg['Subject'] = 'Price Drop Alert'
    msg['From'] = email_id
    msg['To'] = 'email id' # receiver address
    msg.set_content(f'Hey, price of {product} dropped!\n{link}')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)