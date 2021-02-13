DEBUG = False

import RPi.GPIO as GPIO
import dht11
import ambient
import time

CHANNELID='23983'
WRITEKEY='b570ebb66cc48a58' 

#測定する回数
N = 3

#測定する間隔
WAIT = 5

am = ambient.Ambient(CHANNELID, WRITEKEY)

#DHT-11温度・湿度センサはGPIO21に接続されているとする
DHT = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT, GPIO.IN)

#インスタンス作成
sensor = dht11.DHT11(pin=DHT)

counter = 0
temp_total = 0
humi_total = 0

while True:
        #データ取得
        result = sensor.read()

        #有効なデータなら温度湿度を表示
        if result.is_valid():
                temp_total = temp_total +  result.temperature
                humi_total = humi_total +  result.humidity
                counter = counter + 1

                if DEBUG == True:
                        print(temp_total, humi_total)

                if counter >= N:
                        break
                
                time.sleep(WAIT)

temp = temp_total / N
humi = humi_total / N
        
if DEBUG == True:
        print("温度:",temp)
        print("湿度:",humi)

dt =time.strftime("%Y-%m-%d %H:%M:z%S")

data = { 'created': dt, 'd1': temp, 'd2': humi }

if DEBUG == True:
        print(data)

#ambientにアップロード
response = am.send(data)

print(response)
