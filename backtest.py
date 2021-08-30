# 백테스팅
# 과거 데이터로 전략을 테스트 해보는 것

# 업비트 기준
import pyupbit
import numpy as np

# 7일동안의 원화시장의 BTC에 대한 OHLCV를 불러온다.
# OHLCV는 open high low close volume의 약자이고(당일 시가 고자 저가 종가 거래량을 의미)
df = pyupbit.get_ohlcv("KRW-BTC", count = 7)

# 만약 전략 변경을 원하는 경우 변동폭 K값을 변경하면 된다! 

# 다음 두 코드는 변동성 돌파 전략에서 매수가를 구하는 것!
# 변동폭인 (고가 - 저가)랑 k값인 0.5를 곱한값을 range로 저장
df['range'] = (df['high'] - df['low']) * 0.5
# target(매수가), range 칼럼을 한칸씩 밑으로 내림(range 값은 전일의 값이다.), open 은 시가이다.
df['target'] = df['open'] + df['range'].shift(1)
# 그럼 range랑 target 이라는 column 열이 추가가 된다.

# 다음 코드는 수익률을 계산하는 것이다.
# 이는 Numpy 라이브러리를 활용할 것이다. 
# numpy.where는 3가지 인자를 받는다. 1.조건문 2. 조건문이 참일때 값 3. 조건문이 거짓일때 값
# 다음 코드에서 1. high>taget => 고가가 타겟 값보다 높은 경우 
# 2. 종가에 전부 매도 그렇게 되면 수익률은 "종가/목표가" 가 된다
# 3. 매수를 진행하지 않는다. 따라서 수익률은 1
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

# 다음 코드는 누적 수익률을 계산하는 것이다.
# 누적 곱 계산(cumprod) => 누적 수익률 
df['hpr'] = df['ror'].cumprod()
# draw down 계산 (누적 최대 값과 현재 hpr 차이/ 누적 최대값 *100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
# mdd는 dd 중 가장 큰 값을 나타낸다.
print("MDD(%): ", df['dd'].max())
# 이렇게 계산된 값을 엑셀에 저장을 한다! ("dd.xlsx"파일 우클릭 후 reveal in file explore 클릭 후 파일 열기! )
df.to_excel("dd.xlsx")


# 자동매매 코드 구현
# 클라우드 서버에서 돌리기