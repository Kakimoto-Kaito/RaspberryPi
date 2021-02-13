import RPi.GPIO as GPIO
import time

#タッチセンサのSIGピンはGPIO21に接続されているとする
TOUCH=21
#ブザーがGPIO20に接続されているとする
BUZZER=20

#ブザーのON,OFF
ON=GPIO.LOW
OFF=GPIO.HIGH

#ブザーのON/OFF状態の格納する変数
flag=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#タッチセンサが接続されているポートをプルダウンする
GPIO.setup(TOUCH, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUZZER, GPIO.OUT)

GPIO.output(BUZZER, OFF)

#タッチセンサの立ち上がり検出
GPIO.add_event_detect(TOUCH, GPIO.RISING)

try:
        #無限ループ
        while True:
                #タッチセンサがタッチの立ち上がりが検出されたら
                if GPIO.event_detected(TOUCH):
                        if flag ==0:
                                flag=1
                                GPIO.output(BUZZER, ON) 
                                print("ON")
                        else:
                                flag=0
                                GPIO.output(BUZZER, OFF)                
                                print("OFF")
        
                time.sleep(0.5)

except KeyboardInterrupt:
        print("exit")
