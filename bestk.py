import pyupbit
import numpy as np

# 이는 K 값에 따라서 누적 수익률이 어떤 식으로 나오는지 알려준다
# 코드를 실행을 해보면, 최근 하락장에서는 K값이 높을수록 수익률이 높다는 것을 알 수 있다.
# 하지만 k값이 0.5이상이면 전부 1인것을 보아 매수가 진행되지 않아서 수익률이 1인것 같다... 1 이상 수익률이 없다...

def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-DOGE", count = 30)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'],
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror

for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))