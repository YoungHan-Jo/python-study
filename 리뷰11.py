print('=========== 011 ===========')

days_in_month = {'1월':31,'2월':28, '3월':31, '-1월':97889789}

days_in_month.pop('-1월')

print(days_in_month)


print('=========== 012 ===========')

days_in_month = {'1월':31,'2월':28, '3월':31, '4월':30,'5월':31}

for key in days_in_month.keys():
    print(key)


print('=========== 013 ===========')

for key, value in days_in_month.items():
    print(f'{key}은 {value}이 있습니다.')


print('=========== 014 ===========')

import random

list = ['빨','주','노','초','파','남','보']
random_element = random.choice(list)
print(random_element)


print('=========== 015 ===========')

random_number = random.randint(2,5)

print(random_number)


print('=========== 016 ===========')

random.shuffle(list)
print(list)

print('=========== 017 ===========')

import datetime

print(datetime.date.today())

print('=========== 018 ===========')

string1='''
다스베이더가 말했다. 
"내가 니 애비다!"
그 말을 들은 루크는 '깜짝' 놀랐다.'''

list1 = string1.split()

print(list1[4])

print('=========== 019 ===========')

days = [31,29,31,30,31,30,31,31,30,31,30,31]

for n in range(1,13):
    print(f'{n}월의 날짜수는 {days[n-1]}일 입니다')

print('=========== 020 ===========')


a=23
b=5

div = int(a/b)
print(f'a를 b로 나눈 몫은 {div}입니다')