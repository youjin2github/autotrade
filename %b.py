# 지금 가격이 볼린저 밴드 어디에 있는지 나타내는 지표
# 종가가 상단밴드를 태그하면 1, 중간밴드를 태그하면 0.5, 하단밴드를 태그하면0
# 만약 종가가 상단밴드 위에 있으면 1보다 커지고 하단밴드 아래에 있으면 0보다 작아짐

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
df['stddev'] = df['close'].rolling(window=20).std() #20일 이동표준편차
# 여기서 표준편차는 2, 20일 이라고 가정 
df['upper'] = df['ma20'] + 2*df['stddev']  # 위에 띄..? 밴드..?
df['lower'] = df['ma20'] - 2*df['stddev']  # 밑에 거
df = df.assign(PB=(df['close']-df['lower'])/(df['upper']-df['lower']),
밴드폭 = (df['upper']-df['lower'])/df['ma20'])
df = df[19:] # 20일 이동평균을 구했다 따라서 20번째 행부터 값이 들어가 있다.
print(df)
# 여기까지 값이 잘 들어왔는지 우선 확인!

plt.plot(df.index,df['PB'], color='pink',label="%B")
plt.grid(True)
plt.legend(loc='best')
plt.show()
plt.savefig('bollinger band_BTC_2021.12.01~2021.12.22_%b.png')
