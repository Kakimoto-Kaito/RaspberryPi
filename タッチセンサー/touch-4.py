import RPi.GPIO as GPIO
import time

#タッチセンサのSIGピンはGPIO21に接続されているとする
TOUCH=21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#タッチセンサが接続されているポートをプルダウンする
GPIO.setup(TOUCH, GPIO.IN,pull_up_down=GPIO.PUD_UP)

flag=False

#無限ループ
while True:
        #タッチセンサがタッチされたか調べる
        if GPIO.input(TOUCH) == True:
                flag = not flag #flagを反転する（TrueならFalseに、FalseならTrueに）
                if flag == True:
                        print("ON")
                else:
                        print("OFF")
                time.sleep(0.5)
