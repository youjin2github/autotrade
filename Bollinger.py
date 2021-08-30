import pyupbit
import requests
import pandas as pd
import time

from requests.api import head

data=requests.get('')
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

# 로그인
access = "5d57d6zSKTQ5K7zGHEn0vvlQt1me4SWvyx14Czox"        
secret = "Ds5UrNNpFJhP2amtF1LxFO9qWnNu0Gr4o96Qwch7"      
upbit = pyupbit.Upbit(access, secret)
ticker = "KRW-BTC"

# df = pyupbit.get_ohlcv(ticker, interval="day", count=30)         # 분봉 데이터

w= 20 # 기준 이동평균일 
k= 2 # 기준 상수
 
#중심선 (MBB) : n일 이동평균선

df["mbb"]=df["종가"].rolling(w).mean()
df["MA20_std"]=df["종가"].rolling(w).std()

#상한선 (UBB) : 중심선 + (표준편차 × K)
#하한선 (LBB) : 중심선 - (표준편차 × K)
df["ubb"]=df.apply(lambda x: x["mbb"]+k*x["MA20_std"],1)
df["lbb"]=df.apply(lambda x: x["mbb"]-k*x["MA20_std"],1)

# plt.plot(df["mbb"], 'r-',df["ubb"] ,'b-',df["lbb"],'g-')
 
# 밴드를 이탈했다가 진입할 때 거래    
bb_sign=[]
for i in range(len(df)):
    if i<20:
        bb_sign.append("대기")
    elif df.loc[i-1,"종가"]>=df.loc[i-1,"ubb"] and df.loc[i,"종가"]<df.loc[i,"ubb"]:
        bb_sign.append("매도")
    elif df.loc[i-1,"종가"]<df.loc[i-1,"lbb"] and df.loc[i,"종가"]<df.loc[i,"lbb"]:
        bb_sign.append("매수")
    else:
        bb_sign.append("대기")

df["bb_sign"]=bb_sign