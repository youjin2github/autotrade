import pyupbit

# 로그인
access = "5d57d6zSKTQ5K7zGHEn0vvlQt1me4SWvyx14Czox"        
secret = "Ds5UrNNpFJhP2amtF1LxFO9qWnNu0Gr4o96Qwch7"   
upbit = pyupbit.Upbit(access, secret)

# 시장가 매수
upbit.buy_market_order(ticker="KRW-DOGE", price=10000)
# 시장가 매도
upbit.sell_market_order(ticker="KRW-DOGE",price = 10000)