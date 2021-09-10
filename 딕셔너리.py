#딕셔너리는 키와 값ㅇ ㅣ쌍으로 만들어지고 순서 없음, 순정가능, 중복 안됨

#리터럴 생성 (키:값 ) => 키는 문자열, 값은 모든타입가능

person = {
    'name' : '펭수',
    'age' : 30
}

print(type(person))

print(person['name'])
print(person.get('name'))

#키, 값 추가
person['phone'] = '777-7777'
print(person)

# 키, 값, 아이템(key,value) 가져오기
print(person.keys())
print(person.values())
print(person.items())

#아이템 제거
person.pop('phone')
print(person)

#클리어 : 아이템 전부 제거
person.clear()
print(person)