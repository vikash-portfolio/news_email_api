import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "vikash.singh2492@gmail.com"
    password = "vxcyvvxmnhlpbjoy"

    reciever = "vikash.singh2492@gmail.com"
    context = ssl.create_default_context()
    # smtplib.SMTP('smtp.gmail.com', 587)
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)

# send_email("Hi, isthis working ?")
