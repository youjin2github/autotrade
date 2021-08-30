import pyupbit

access = "5d57d6zSKTQ5K7zGHEn0vvlQt1me4SWvyx14Czox"        
secret = "Ds5UrNNpFJhP2amtF1LxFO9qWnNu0Gr4o96Qwch7" 

# """변동성 돌파 전략으로 매수 목표가 조회"""
def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="minute60", count=36)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

print(get_target_price("KRW-DOGE",0.7))