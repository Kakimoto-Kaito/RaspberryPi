import RPi.GPIO as GPIO
import dht11
import time

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
                print("温度:",result.temperature)
                print("湿度:",result.humidity)

        #2秒休止
        time.sleep(2)
