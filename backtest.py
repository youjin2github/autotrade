# 백테스트 코드
import pyupbit
import pandas as pd
import numpy as np

df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="minute60",count=620)

# 로그인
access = "5d57d6zSKTQ5K7zGHEn0vvlQt1me4SWvyx14Czox"        
secret = "Ds5UrNNpFJhP2amtF1LxFO9qWnNu0Gr4o96Qwch7"   
upbit = pyupbit.Upbit(access, secret)

ticker = "KRW-BTC"

#  """현재가 조회"""
def get_current_price(ticker):
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]
# print(get_current_price(ticker))

df = pyupbit.get_ohlcv(ticker=ticker, interval="minute60",count=619) # 1시간 봉 데이터
# 열 이름 만들어주기
df = df.rename(columns={0:"time",1:"open", 2:"high", 3:"low",4:"close",5:"volume"})
# 볼린저 밴드 항목 추가하기
df['ma20'] = df['close'].rolling(window = 20).mean() #20일 이동평균
df['stddev'] = df['close'].rolling(window = 20).std() #20일 이동표준편차
# 여기서 표준편차는 2, 20일 이라고 가정 
# df['upper'] = df['ma20'] + 2*df['stddev']  # 위에 띄..? 밴드..?
df['lower'] = df['ma20'] - 2*df['stddev']  # 밑에 거
lower = df['lower'] = df['ma20'] - 2*df['stddev']
df = df[19:] # 20일 이동평균을 구했다 따라서 20번째 행부터 값이 들어가 있다
lower = lower[19:]
print(lower.head()*1.01)
print(lower.head())

current_60_price = pyupbit.get_ohlcv(ticker=ticker, interval="minute60",count = 600) # 1시간 봉 데이터
current_60_price_close = current_60_price['close']
df['current_60_price_close'] = current_60_price['close']
print(current_60_price_close.head())
df['target'] = df['open'].shift(1)

df['볼밴하단*1.01'] = lower*1.01
df['ror'] = np.where(lower*1.01 > current_60_price_close,
                     df['target']/current_60_price_close,
                     1)
# print(df['ror'])
df['ror'].to_excel("df['ror'].xlsx")
df['hpr'] = df['ror'].cumprod()
df['hpr'].to_excel("df['hpr'].xlsx")
df.to_excel("df.xlsx")
