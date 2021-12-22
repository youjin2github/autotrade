import pyupbit
import matplotlib.pyplot as plt

ticker = "KRW-BTC"
df = pyupbit.get_ohlcv(ticker=ticker, interval="minute60",count=480) # 1시간 봉 데이터
print(df)
# 열 이름 만들어주기
df = df.rename(columns={0:"time",1:"open", 2:"high", 3:"low",4:"close",5:"volume"})
print(df)
# 볼린저 밴드 항목 추가하기
df['ma20'] = df['close'].rolling(window = 20).mean() #20일 이동평균
df['stddev'] = df['close'].rolling(window = 20).std() #20일 이동표준편차
# 여기서 표준편차는 2, 20일 이라고 가정 
df['upper'] = df['ma20'] + 2*df['stddev']  # 위에 띄..? 밴드..?
df['lower'] = df['ma20'] - 2*df['stddev']  # 밑에 거
df = df[19:] # 20일 이동평균을 구했다 따라서 20번째 행부터 값이 들어가 있다
print(df)
# 여기까지 실행을 완료했을때 NA라고 뜨는게 없어야 한다!
plt.figure(figsize=(9,5))
# plt.plot(df.index, df["close"] ,label = 'close')
plt.plot(df.index, df['upper'], linestyle = 'dashed',label = 'Upper band')
plt.plot(df.index, df['lower'], linestyle = 'dashed',label = 'Lower band')
# plt.plot(df.index, df['ma20'], linestyle = 'dotted',label = 'Moving Average 20')
plt.title(f'{"BTC"} 2021_bollinger band(day = 20, std = 2)')
plt.legend(loc='best')
plt.show()
plt.savefig('bollinger band_BTC_2021.12.02~2021.12.22.png')
