import pyupbit


# print(upbit.get_balance('KRW'))   

# 도달가 매수 매도
# price_BTC = pyupbit.get_current_price("KRW-BTC")
# 지금 가격을 조회
# price = format(price_BTC)
# print(price*0.97)
# target_price = price*0.97
# print(target_price)
#  if target_price < price:
#                 krw = get_balance("KRW")
#                 if krw > 5000:
#                     upbit.buy_market_order("KRW-BTC", krw*0.9995)


# 매수
# print(upbit.buy_limit_order("KRW-BTC", price*0.97, 0.001))
# 매도
# print(upbit.sell_limit_order("KRW-BTC", 38000000, 0.001))

# -90퍼센트에 도달하면 자동으로 매수하여 다음날 종가에 매도하는 알고리즘

# 물어볼것! -90퍼센트가 09:00 기준 -90퍼센트인지 아니면 1시간봉 기준 -90퍼센트인지?!

# -90퍼센트가 당일 09:00 기준 대비 하락된 퍼센트라고 가정
# 암호화폐의 open 가격 확인(비트코인 기준으로 작성!)
# df = pyupbit.get_ohlcv("KRW-BTC",count = 1) 
# df_open = df["open"]
# print(df_open)
# df_open_90 = df["open"]*0.1
# print(df_open_90)
# # 다음날 종가 확인
# df = pyupbit.get_ohlcv("KRW-BTC",count = 1)
# 매수
# print(upbit.buy_limit_order("KRW-BTC", 38400000, 0.001))
# 매도
# print(upbit.sell_limit_order("KRW-BTC", 38000000, 0.001))