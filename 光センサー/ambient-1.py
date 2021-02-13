import ambient
import time

CHANNELID = '23968'
WRITEKEY = '93caffa475fa5dc8'

#インスタンス作成
am = ambient.Ambient(CHANNELID, WRITEKEY)

#現在日時取得
dt = time.strftime("%Y-%m-%d %H:%M:%S")

#現在秒を取得し、データとして使用する
s = time.strftime("%S")

#送信データ作成
data = { 'created': dt, 'd1': s}

#送信データ表示
print(data)

#ambientにデータを送信
response = am.send(data)

#ambientからのレスポンスを表示
print(response)
