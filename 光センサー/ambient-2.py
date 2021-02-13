import RPi.GPIO as GPIO
import dht11
import ambient
import time

CHANNELID='23983'
WRITEKEY='b570ebb66cc48a58' 

am = ambient.Ambient(CHANNELID, WRITEKEY)

#DHT-11温度・湿度センサはGPIO21に接続されているとする
DHT = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT, GPIO.IN)

#インスタンス作成
sensor = dht11.DHT11(pin=DHT)

while True:
        #データ取得
        result = sensor.read()

        #有効なデータなら温度湿度を表示
        if result.is_valid():
                temp = result.temperature
                humi = result.humidity
        
                print("温度:",temp)
                print("湿度:",humi)

                dt =time.strftime("%Y-%m-%d %H:%M:z%S")

                data = { 'created': dt, 'd1': temp, 'd2': humi }
                print(data)

                #ambientにアップロード
                response = am.send(data)

                print(response)

                break
