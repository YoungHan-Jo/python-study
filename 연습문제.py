# a = "Life is too short, you need python"

# if "wife" in a: 
#     print("wife")
# elif "python" in a and "you" not in a: 
#     print("python")
# elif "shirt" not in a: 
#     print("shirt")
# elif "need" in a: 
#     print("need")
# else: 
#     print("none")

i = 0
sum = 0

while i <= 1000:
    if i%3 == 0:
        sum += i
    i += 1

print(sum)

print('========================')

n = 5
i = 1
while i <= n:
    print('*'*i)
    i += 1

print('=========================')
print('보물섬에 온 것을 환영합니다.\n보물을 찾아보세요')

if input('당신은 갈림길을 만났습니다.\n왼쪽or오른쪽을 적어서 선택 : ') == '왼쪽':
    print('갈림길을 통과했습니다.')
    if input('바다가 있습니다. 건너겠습니까?\n수영or대기 적어서 선택 : ') == '대기':
        print('기다리니 문이 나왔습니다.')
        door = input('문을 선택하세요.\n노란색or빨간색or파란색 중 선택 : ')
        if door =='노란색':
            print('축하합니다. 게임에서 승리!')
        elif door =='빨간색':
            print('불에 타서 사망')
        elif door =='파란색':
            print('괴물에게 먹힘 사망')
        else:
            print('게임오버')
    else:
        print('상어의 공격으로 사망')
else:
    print('함정에 빠져 사망')