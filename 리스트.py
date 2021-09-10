#리스트는 순서가 있고 수정가능한 자료구조. 값이 중복가능

#리터럴로 만들기
fruits = ['사과','오렌지','포도','배','망고']
print(fruits)
print(len(fruits))

fruits.remove('포도')
print(fruits)
fruits.insert(2, '딸기')
print(fruits)

#특정인덱스 값 제거
fruits.pop(3)
print(fruits)

#리버스 리스트 : 리스트 순서를 거꾸로
fruits.reverse()
print(fruits)

# 정렬 sort() : 알파벳 순, 한글 순
fruits.sort()
print(fruits)
#거꾸로정렬
fruits.sort(reverse=True)
print(fruits)