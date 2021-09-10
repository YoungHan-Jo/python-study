#내장함수

#리스트
list('python') #['p', 'y', 't', 'h', 'o', 'n']

#max() 최대값, min() 최소값
#sum() 합계,

#range(시작,끝,(증감)) : 시작부터 끝-1 까지

#함수 작성
def sayHello(name='펭수'): #디폴트값 설정
    '''이 함수는 헬로우를 출력'''
    print('헬로우 ' + name)

sayHello()
sayHello('길동')

def getSum(n1,n2):
    total = n1 + n2
    return total

print(getSum(1,2))

print('================예제1===================')

def is_odd(num):
    if num%2 == 0:
        print('짝수')
    else:
        print('홀수')

is_odd(1)
is_odd(2)

print('================예제2===================')
def avgNums(*num):
    sum = 0
    for n in num:
        sum += n
    avg = sum / len(num)
    return avg

print(avgNums(1,2,3))
print(avgNums(1,2,3,4,5,6,7,8,9,10))