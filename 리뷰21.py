print('=========== 021 ===========')

numbers = [1,2,3]
length = len(numbers)
i = 0
while i < length:
    print(numbers[i])
    i += 1

print('=========== 022 ===========')

sizes = [33,35,34,37,32,35,39,32,35,29]
for i,size in enumerate(sizes):
    if size == 32:
        print(f'사이즈 32인 바지는 {i+1}번째에 있다.')
        break

print('=========== 023 ===========')

try:
    a = 3/0
except Exception:
    print('0으로 나눌 수 없습니다.')


print('=========== 024 ===========')

try:
    a = 5
    b = 0
    c = a/b
except Exception as ex:
    print(f'다음과 같은 에러가 발생했습니다 : {ex}')

print('=========== 025 ===========')

if []:
    print("[]은 True입니다.")

if [1, 2, 3]:
    print("[1,2,3]은/는 True입니다.")

if {}:
    print("{}은 True입니다.")

if {'abc': 1}:
    print("{'abc':1}은 True입니다.")

if 0:
    print("0은/는 True입니다.")

if 1:
    print("1은 True입니다.")

print('=========== 026 ===========')

a = 1 or 10
b = 0 or 10

print(f'a:{a}, b:{b}')

print('=========== 027 ===========')

list1 = [1,2,3,4]

list1.insert(1,8)
print('첫 번째 자리에 8을 넣은결과 : {}'.format(list1))

list1.sort()
print('작은 수 부터 큰 수로 정렬 : {}'.format(list1))

list1.reverse()
print('큰 수 부터 작은수로 정렬 : {}'.format(list1))





print('=========== 028 ===========')

str = '오늘은 날씨가 흐림'

words = str.split()

position = words.index('흐림')
words[position] = '맑음'

new_str = ' '.join(words)

print(new_str)



print('=========== 029 ===========')

rainbow = ['빨','주','노','초','파','남','보']

red_colors = rainbow[0:3]
print('red_colors의 값 : {}'.format(red_colors))
blue_colors = rainbow[4:7]
print('blue_colors의 값 : {}'.format(blue_colors))