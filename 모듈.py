import random
import my_module as my

random_side = random.randint(0,1)

if random_side == 1:
    print('앞면')
else:
    print('뒷면')

print(my.pi)

# 모듈은 프로그래밍을 할때 필요한 함수들을 모아놓은 파일이다.
# 중요 파이썬 모듈들은 이미 설치되어 있고 커스텀 모듈들은 패키지 매니저 pip로 설치한다.

#중요모듈 예
import datetime
import time

today = datetime.date.today()
print(today)

timestamp = time.time()
print(timestamp)

#커스텀 모듈 설치 pip install 을 사용해서 설치를 한다.
import camelcase

camel = camelcase.CamelCase()
text = 'hello there world'
print(camel.hump(text))