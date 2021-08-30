import pyupbit
# 로그인
access = "5d57d6zSKTQ5K7zGHEn0vvlQt1me4SWvyx14Czox"        
secret = "Ds5UrNNpFJhP2amtF1LxFO9qWnNu0Gr4o96Qwch7"         
upbit = pyupbit.Upbit(access, secret)
# 암호화폐 목록 가져오기 
print(pyupbit.get_tickers())
# 특정 시장에만 거래 가능한 암호화폐 목록 가져오기 (KRW/BTC/USDT)
print(pyupbit.get_tickers(fiat="KRW"))
# python coinlist.py