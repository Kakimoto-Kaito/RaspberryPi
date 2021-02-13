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

DATAFILE = "data.txt"
with open(DATAFILE, mode='a') as f:
        f.write(data)

t = time.strftime("%Y/%m/%d %H:%M:%S")

for i in renge(5):

while True:
        #データ取得
        result = sensor.read()

        #有効なデータなら温度湿度を表示
        if result.is_valid():
                print(t, result.temperature, result.humidity)

        break
