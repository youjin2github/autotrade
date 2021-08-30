import time
import pyupbit
import datetime

def get_target_price(DOGE, k):
    df = pyupbit.get_ohlcv(DOGE, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price
print(get_target_price)