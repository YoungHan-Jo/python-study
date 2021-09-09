#불리언 타입은 참/거짓 True/False
mybool1 = True
mybool2 = False
print(type(mybool1))
print(mybool1)

mybool3 = 1 < 2
mybool4 = 1 == 2
print(mybool3)
print(mybool4)

# bool타입으로 변환 시 True False 외의 값들은 0을 제외하고 모두 True로 변환
print(bool(1))
print(bool(0))

print(bool('1'))
print(bool('불리언'))

# 논리 연산자 and or not
# and

print(True and True)
print(True and False)
print(False and True)
print(False and False)
