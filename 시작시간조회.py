import pyupbit

#  """시작 시간 조회"""
def get_start_time(ticker):

    df = pyupbit.get_ohlcv(ticker, interval="day", count=7)
    start_time = df.index[0]
    return start_time

print(get_start_time("KRW-DOGE"))