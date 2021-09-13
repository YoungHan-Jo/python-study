#파일 읽기 모드 'r'
f = open('fruits.txt','r',encoding='utf-8')

print(f.read())

f.close() #파일 닫기

# 파일 닫기 자동으로 하기
with open('fruits.txt','r',encoding='utf-8') as f:
    print(f.read())

#파일 쓰기 (파일이 없으면 새로 생성)
with open('vegi.txt','w',encoding='utf-8') as f1:
    f1.write('무\n')
    f1.write('배추\n')
    f1.write('토마토\n')
    f1.write('브로콜리\n')

#붙여쓰기 'a'
with open('vegi.txt','a',encoding='utf-8') as f2:
    f2.write('고추\n')


with open('vegi.txt','r',encoding='utf-8') as f3:
    print(f3.read())