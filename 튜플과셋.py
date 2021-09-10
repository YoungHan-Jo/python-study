# 튜플은 순서가 있고 수정불가인 자료구조 입니다. 중복은 가능

# 리터럴 생성 () 괄호 사용
fruit_tuple=('사과','오렌지','망고')
#생성자
fruit_tuple= tuple(('사과','오렌지','망고'))
print(type(fruit_tuple))
#값을 가져오기
print(fruit_tuple[1])

#튜플의 값이 1개인 경우에 콤마 필요
fruit_tuple2 = ('사과',)

#길이
print(len(fruit_tuple))

# 튜플은 수정 불가
# fruit_tuple[1] = '딸기'

# 튜플 객체 삭제
del fruit_tuple2

#SET셋은 순서가 없고 중복이 안되는 자료구조
# 만들때 {} 중괄호
fruit_set = {'사과','오렌지','망고'}
print(type(fruit_set))

print('사과'in fruit_set)

#추가
fruit_set.add('포도')
print(fruit_set)
#같은거 중복 안됨
fruit_set.add('포도')
print(fruit_set)

#클리어: 모든아이템 삭제
fruit_set.clear()
print(fruit_set)