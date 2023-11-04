import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "de.chandra226@gmail.com"
    password = st.secrets['YOUR_GMAIL_SMTP_PASSWORD']
    receiver = "de.chandra226@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
