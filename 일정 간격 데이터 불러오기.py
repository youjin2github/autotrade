import pyupbit

ticker = "KRW-DOGE"

pyupbit.get_ohlcv(ticker=ticker, interval="minute1")  # 분봉 데이터
pyupbit.get_ohlcv(ticker=ticker, interval="minute3")  # 3분봉 데이터
pyupbit.get_ohlcv(ticker=ticker, interval="minute5")  # 5분봉 데이터
pyupbit.get_ohlcv(ticker=ticker, interval="minute10") # 10분봉 데이터
pyupbit.get_ohlcv(ticker=ticker, interval="minute30") # 30분봉 데이터
pyupbit.get_ohlcv(ticker=ticker, interval="minute60") # 1시간 봉 데이터
pyupbit.get_ohlcv(ticker=ticker, interval="minute240") # 4시간 봉 데이터 
pyupbit.get_ohlcv(ticker=ticker, interval="week")  # 주봉 데이터
pyupbit.get_ohlcv(ticker=ticker, interval="month")  # 월봉 데이터

minute60 = pyupbit.get_ohlcv(ticker=ticker, interval="minute60") # 1시간 봉 데이터
print(minute60)