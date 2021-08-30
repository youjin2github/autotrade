import time
import pyupbit
import datetime

access = "5d57d6zSKTQ5K7zGHEn0vvlQt1me4SWvyx14Czox"        
secret = "Ds5UrNNpFJhP2amtF1LxFO9qWnNu0Gr4o96Qwch7" 

ticker = "KRW-DOGE"

# """변동성 돌파 전략으로 매수 목표가 조회"""
def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=36)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

#  """시작 시간 조회"""
def get_start_time(ticker):

    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

#  """잔고 조회"""
def get_balance(ticker):
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

#  """현재가 조회"""
def get_current_price(ticker):
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-DOGE") # 9:00
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price = get_target_price("KRW-DOGE", 0.7)
            current_price = get_current_price("KRW-DOGE")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-DOGE", krw*0.9995)
        else:
            doge = get_balance("DOGE")
            if doge > 50:
                upbit.sell_market_order("KRW-DOGE", doge*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
