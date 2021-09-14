# #01
# num1 = int(input('정수1:'))
# num2 = int(input('정수2:'))

# print(f'합은: {num1+num2} 입니다.')

# #02
# num1 = int(input('first number:'))
# num2 = int(input('second number:'))
# print(f'add: {num1+num2}')
# print(f'sub: {num1-num2}')
# print(f'mul: {num1*num2}')
# print(f'div: {num1/num2}')

# #03
# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i} x {j} = {i*j}\t',end='')
#     print()

# #05
# def easy_unpack(elements):
#     return (elements[0], elements[2], elements[-2] )  # 튜플로 리턴

# if __name__ == '__main__':
#     print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
#     assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
#     assert easy_unpack((6, 3, 7)) == (6, 7, 3)

# #06
# def is_acceptable_password(password):
#     return len(password)>6
    
# if __name__ == '__main__':
#     print(is_acceptable_password('short'))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert is_acceptable_password('short') == False
#     assert is_acceptable_password('muchlonger') == True
#     assert is_acceptable_password('ashort') == False

# #07
# def number_length(a):
#     return len(str(a))

# if __name__ == '__main__':
#     print(number_length(10))

#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert number_length(10) == 2
#     assert number_length(0) == 1
#     assert number_length(4) == 1
#     assert number_length(44) == 2

# #08
# def remove_all_before(items, i) :
#     if i in items:
#         num = items.index(i)
#         return items[num::]
#     return items 

# if __name__ == '__main__':
#     print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
    
#     # 다음과 같이 리턴결과가 나와야 한다.
#     assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
#     assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
#     assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
#     assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
#     assert list(remove_all_before([], 0)) == []
#     assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]

#09

def replace_first(items):
    if len(items)>2:
        temp = items[0]
        items = items[1::]
        items.append(temp)
    return items
   

if __name__ == '__main__':
    print(list(replace_first([1, 2, 3, 4])))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []