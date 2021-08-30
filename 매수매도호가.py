import pyupbit
# 로그인
access = "5d57d6zSKTQ5K7zGHEn0vvlQt1me4SWvyx14Czox"        
secret = "Ds5UrNNpFJhP2amtF1LxFO9qWnNu0Gr4o96Qwch7"
# 매수/매도 호가 정보 조회    
# tickers 안에 여러개의 암호화폐를 추가하여 한번에 불러오기 가능

# market : 암호화폐 티커
# timestamp : 조회시간 (단위 ms)
# orderbook_units : 매도호가/매수호가 정보
# 이 순서로 자료가 나타난다.
print(pyupbit.get_orderbook(tickers="KRW-BTC"))
# python 매수매도호가.py