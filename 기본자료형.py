# 정수int, 실수 float

print(2+4)
print(2-4)
print(2*4)
print(2/4)

#type() 함수 : 타입을 알려준다.
print(type(1))
print(type(0.1))

print(9.9+1.1) #자동 타입변환 안됨

#제곱과 나누기
print(2**4) # 거듭제곱
print(5//2) # 몫
print(5%2) #나머지

# 반올림
print(round(3.6463,2))
# 절대값
print(abs(-20))

a, b, c = 1, 2, 3
print(a,b,c)

print('===========================')
#예제 2
x = 10
print(x)

#예제 3
x,y,z = 1,2,3
print(x,y,z)

#예제 4
x = 1
y = 1.2
z = 'a'

print(type(x))
print(type(y))
print(type(z))

# 예제5
a = input('a : ')
b = input('b : ')

a,b=b,a

print('a : ' + a)
print('b : ' + b)
