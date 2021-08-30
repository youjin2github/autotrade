import pybithumb
import requests
import pandas as pd
import time

from requests.api import head

data=requests.get('https://api.bithumb.com/public/candlestick/BTC_KRW/24h')
data=data.json()
data=data.get("data")
df=pd.DataFrame(data)

df.rename(columns={0:"time",1:"시가", 2:"종가", 3:"고가",4:"저가",5:"거래량"}, inplace=True)
df.sort_values("time", inplace=True)
df=df.tail(365)
df=df[['time',"시가", "종가", "고가","저가","거래량"]].astype("float")
df.reset_index(drop=True, inplace=True)
df["date"]=df["time"].apply(lambda x:time.strftime('%Y-%m-%d %H:%M', time.localtime(x/1000)))
print(df)

# df.sort_values("time",inplace=True)

# df.rename(columns={0:'time',1:"시가", 2:"종가", 3:"고가",4:"저가",5:"거래량"}, inplace=True)
# df.sort_values("time", inplace=True)
# df=df.tail(365)
# df=df[['time',"시가", "종가", "고가","저가","거래량"]].astype("float")
# df.reset_index(drop=True, inplace=True)

print(df)

# import time
# import pyupbit
# import datetime
# import numpy as np

# # 로그인
# access = "5d57d6zSKTQ5K7zGHEn0vvlQt1me4SWvyx14Czox"        
# secret = "Ds5UrNNpFJhP2amtF1LxFO9qWnNu0Gr4o96Qwch7"      
# upbit = pyupbit.Upbit(access, secret)
# ticker = "KRW-BTC"

# # OHLCV는 open high low close volume의 약자이고(당일 시가 고자 저가 종가 거래량을 의미)
# df = pyupbit.get_ohlcv(ticker)
# # 시간 봉 
# w= 20 # 기준 이동평균일 
# k= 2 # 기준 상수
 
# #중심선 (MBB) : n일 이동평균선
# df["mbb"]=df["open"].rolling(w).mean()
# df["MA20_std"]=df["open"].rolling(w).std()
# df["ubb"]=df.apply(lambda x: x["mbb"]+k*x["MA20_std"],1)
# df["lbb"]=df.apply(lambda x: x["mbb"]-k*x["MA20_std"],1)

# print(df["mbb"])
# print(df["MA20_std"])

# a = df[['mbb','ubb','lbb','close']]

# a=df[['close','mbb', 'ubb', 'lbb']][-200:]
 
# b=df[["mbb","MA20_std","ubb","lbb"]].fillna(0, inplace=True)

# plt.plot(a)
# plt.plot(b)
# plt.show()