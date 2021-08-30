import pyupbit
# 로그인
access = "5d57d6zSKTQ5K7zGHEn0vvlQt1me4SWvyx14Czox"        
secret = "Ds5UrNNpFJhP2amtF1LxFO9qWnNu0Gr4o96Qwch7"         
upbit = pyupbit.Upbit(access, secret)
# 암호화폐의 현재가격을 불러오기
print(pyupbit.get_current_price("KRW-BTC"))
# 원하는 암호화폐를 coinlist에서 추출해서 get_current_price("")안에 대입, 최대 100개 가능
# python 최근거래가격.py