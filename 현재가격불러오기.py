import pyupbit

DOGE_PRICE = pyupbit.get_current_price("KRW-DOGE")
print(DOGE_PRICE)
