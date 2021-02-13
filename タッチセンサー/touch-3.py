import RPi.GPIO as GPIO
import time

#タッチセンサのSIGピンはGPIO21に接続されているとする
TOUCH=21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#タッチセンサが接続されているポートをプルダウンする
GPIO.setup(TOUCH, GPIO.IN,pull_up_down=GPIO.PUD_UP)

#無限ループ
while True:
        #タッチセンサがタッチされたか調べる
        if GPIO.input(TOUCH)==True:
                print(time.strftime("%Y/%m/%d %H:%m:%S"),"ON")
        #0.1秒間休止する
        time.sleep(0.1)
