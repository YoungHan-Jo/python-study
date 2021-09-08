# 문자열에 인덱스번호가 있음
# string1 = '영일이삼사'
# print(string1[0])
# print(string1[1])
# print(string1[2])
# print(string1[3])
# print(string1[4])

#문자열의 슬라이싱 [시작:끝:(증감)]
# text = '영일이삼사'
# print(text[1:5]) # 1부터 5-1 까지
# print(text[3:]) #3부터 끝까지
# print(text[:3]) #처음부터 3-1 까지
# print(text[:]) #전체
# #증감
# print(text[::-1])
# print(text[::2])

# # 문자열 길이 len()
# print(len(text))

# #코드 실행순서
# print('안녕하세요 ' + input('당신의 이름은 ? ') + '님')

#Ex 1
two_digit_number = input('두 자리 숫자를 입력 : \n')

result = int(two_digit_number[0]) + int(two_digit_number[1])

print('두 숫자의 합은 {} 입니다.'.format(result))

print('=============================')

height = input('키를 미터 단위로 입력하세요 : ')
weight = input('몸무게를 키로 단위로 입력하세요 : ')

bmi = float(weight) / float(height)**2

print(f'당신의 bmi 는 {round(bmi,2)} 입니다.')