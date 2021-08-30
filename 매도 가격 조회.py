import pyupbit


access = "5d57d6zSKTQ5K7zGHEn0vvlQt1me4SWvyx14Czox"        
secret = "Ds5UrNNpFJhP2amtF1LxFO9qWnNu0Gr4o96Qwch7" 

ticker = "KRW-DOGE"

# 매도 가격 조회
def get_sell_price(ticker):
    df = pyupbit.get_ohlcv(ticker)
    sell_price = df.iloc[0]['close'] 
    return sell_price

print(get_sell_price("KRW-DOGE"))