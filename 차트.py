import pyupbit
# 로그인
access = "5d57d6zSKTQ5K7zGHEn0vvlQt1me4SWvyx14Czox"        
secret = "Ds5UrNNpFJhP2amtF1LxFO9qWnNu0Gr4o96Qwch7"    

# 고가/시가/저가/종가/거래량을 DataFrame으로 반환
# count는 영업일을 의미, count = 5는 영업일의 고가/시가/저가/종가/거래량을 나타냄
df = pyupbit.get_ohlcv("KRW-BTC",count = 5)
print(df.tail())
# 200개의 자료를 불러오는 방법
df = pyupbit.get_ohlcv("KRW-BTC", count=600, period=1)
# interval로 day/minute1/minute3/minute5/minute10/minute15/minute30/minute60/minute240/week/month 설정 가능
# 1시간봉 데이터 => 이게 기준이라고 했었음!!
print(pyupbit.get_ohlcv("KRW-BTC",interval="minute60"))
# python 차트.py