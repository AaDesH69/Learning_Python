# -*- coding: utf-8 -*-
import haloboard
import time
import event

@event.start
def use_code():
    haloboard.wifi.start(ssid = "Maker-guest", password = "makeblock", mode = haloboard.wifi.WLAN_MODE_STA)

    while(True):
        if haloboard.wifi.is_connected() == True:
            print("wifi is connected!")
            break;

    while True:
        if haloboard.button.is_pressed():
            haloboard.led.show_all(0, 0, 50)
            haloboard.speech_recognition.start(haloboard.speech_recognition.SERVER_MICROSOFT, haloboard.speech_recognition.LAN_DEFAULT, 2)
            if haloboard.speech_recognition.get_error_code() != 0:
                str = haloboard.speech_recognition.get_error_message()
                print("error_message:" + str)
            else:
                result = haloboard.speech_recognition.get_result_code()
                print("result:" + result)
                if '红色' in result:
                    haloboard.led.show_all(50, 0, 0)
                elif '黄色' in result:
                    haloboard.led.show_all(50, 50, 0)
                elif '白色' in result:
                    haloboard.led.show_all(50, 50, 50)
                elif '蓝色' in result:
                    haloboard.led.show_all(0, 0, 50)
                elif '绿色' in result:
                    haloboard.led.show_all(0, 50, 0)
                else:
                    haloboard.led.show_all(0, 0, 0)
        time.sleep(0.5)