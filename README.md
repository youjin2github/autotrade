# 볼린저밴드 활용 : 비트코인 자동매매


### 볼린저밴드란?
볼린저 밴드는 주가가 이동평균선 중심으로 표준편차 범위 안에서 움직인다는 전제로 개발된 변동성 지표이다.
이를 활용하여 차트를 분석하고 자동매매 코드를 구현할 것이다

## 🙋 Contributors
|담당|이름|
|---|---|
|아이디어 & 분석|[김홍길]
|분석 & 모델링|[김유진]

## ✍️ Projects

2021.06.01~진행중


### ✔Process

1. 💾[데이터 수집]
    * [API로그인](https://github.com/youjin2github/autotrade/blob/main/login.py)
    * [코인 종류 불러오기](https://github.com/youjin2github/autotrade/blob/main/coinlist.py)
    * [일정 간격 가격 불러오기](https://github.com/youjin2github/autotrade/blob/main/%EC%9D%BC%EC%A0%95%20%EA%B0%84%EA%B2%A9%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%88%EB%9F%AC%EC%98%A4%EA%B8%B0.py)
    * [잔고조회](https://github.com/youjin2github/autotrade/blob/main/%EC%9E%94%EA%B3%A0%EC%A1%B0%ED%9A%8C.py)
    * [현재가격조회](https://github.com/youjin2github/autotrade/blob/main/%ED%98%84%EC%9E%AC%EA%B0%80%EA%B2%A9%EB%B6%88%EB%9F%AC%EC%98%A4%EA%B8%B0.py)
   
   
2. 🧩[주문하기]
    * [시장가격매수매도](https://github.com/youjin2github/autotrade/blob/main/%EC%8B%9C%EC%9E%A5%EA%B0%80%20%EC%A3%BC%EB%AC%B8%ED%95%98%EA%B8%B0.py)
    * 지정가격매수매도
    

3. 💡[볼린저밴드분석]
    * [볼린저밴드 그래프 그리기](https://github.com/youjin2github/autotrade/blob/main/%EA%B7%B8%EB%9E%98%ED%94%84%EA%B7%B8%EB%A6%AC%EA%B8%B0.py)
    * [밴드폭 그래프 그리기](https://github.com/youjin2github/autotrade/blob/main/%EB%B0%B4%EB%93%9C%ED%8F%AD%2Cpy)
    * [%b 그래프 그리기](https://github.com/youjin2github/autotrade/blob/main/%25b.py)
    * [예상 수익률 backtest를 통해 확인](https://github.com/youjin2github/autotrade/blob/main/backtest.py)


4. 💡[변동성 돌파 전략]
    * [자동매매코드 => 유투버 : 조코딩 참조](https://github.com/youjin2github/autotrade/blob/main/bitcoinAutoTrade.py)


5. ☁[클라우드 서버 돌리기(초간단)]
    * [AWS(UBUNTU)활용](https://ap-northeast-2.console.aws.amazon.com/ec2/v2/home?region=ap-northeast-2#Home:)
    * [해당 방법으로 실행!](https://github.com/youjin2github/autotrade/blob/main/%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C%20%EC%84%9C%EB%B2%84%20AWS(UBUNTU))

   
