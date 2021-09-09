import random

# 🚨 여기는 그대로 👇
names_string = input("내기를 할 친구들의 이름을 적습니다. 콤마(,)로 분리해서 적습니다.\n")
names = names_string.split(",")
# 🚨 여기는 그대로 👆

#아래에 코드 작성 👇
randIndex = random.randint(0,len(names)-1)
print(f'오늘의 점심은 {names[randIndex]} 님이 쏩니다.')
