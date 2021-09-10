#001 함수 만들기

print('=========== 001 ===========')

def add(a,b):
    print(f'{a} + {b} = {a+b}')
    
add(10,5)

print('=========== 002 ===========')

def add(a,b):
    return a + b

print(add(10,5))

print('=========== 003 ===========')

rainbow = ['빨강','주황','노랑','초록','파랑','남색','보라']

first_color = rainbow[0]

print(f'무지개의 첫번째 색은 {first_color}이다.')

print('=========== 004 ===========')

last_color = rainbow[-1]
print(f'무지개의 마지막 색은 {last_color} 이다.')

print('=========== 005 ===========')

list = [1,2,3]
list.append(4)
print(list)
list = [1,2,3]
list += [4]
print(list)

print('=========== 006 ===========')
numbers = [1,2,3,4,5]
n = 5

if n in numbers:
    print(f'{n}가 리스트에 있다.')

print('=========== 007 ===========')

list1=[1,2,3]
list1.remove(2)
print(list1)

print('=========== 008 ===========')

days_in_month = {
    '1월': 31,
    '2월': 28,
    '3월': 31
}

print(days_in_month)

print('=========== 009 ===========')

person = {
    '이름': '홍길동',
    '번호': 1010,
    '취미': ['낮잠','숨쉬기','커피']
}

print(person)

print('=========== 010 ===========')

days_in_month['2월'] = 29

print(days_in_month)




















