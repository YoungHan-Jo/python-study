# #if 문
# name = '앨리스'
# if name == '앨리스':
#     print('반가워요 ' + name)
#     print('앞에 띄어쓰기가 있으면 포함')

# print('종료')

# if elif else 문
# name = '밥'
# if name == '앨리스':
#     print('반가워요'+name)
# elif name == '펭수':
#     print('반가워요'+name)
# else:
#     print('누구신가요?')

# #Ex1
# number = int(input("숫자를 입력 : \n"))

# if number%2 == 0:
#     print('짝수 입니다.')
# else:
#     print('홀수 입니다.')


height = int(input('키를 cm로 입력해 주세요 : \n'))

if height > 120:
    print('청룡열차를 탈 수 있습니다.')
    age = int(input('나이를 입력해 주세요 : \n'))
    if age > 18 :
        print('요금은 12000원 입니다.')
    elif age >=12:
        print('요금은 7000원 입니다.')
    else:
        print('요금은 5000원 입니다.')

else:
    print('청룡열차를 탈 수 없습니다.')