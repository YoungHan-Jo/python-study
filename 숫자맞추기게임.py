import random

randomNumber = random.randint(1,20)
chance = 5
challenge = 0

name = input('당신의 이름은? \n')
print(f'안녕하세요 {name}님 , 1에서 20까지 숫자 중 하나를 생각합니다.')

while chance >=0:
    if chance == 0:
        print(f'기회를 모두 사용했습니다. 정답은 {randomNumber} 입니다. 다시 도전하세요')
        break

    answer = int(input(f'맞춰보세요 (남은 기회: {chance}) \n'))
    challenge += 1;

    if answer > 0 and answer <21:
        if randomNumber > answer:
            print(f'{answer}보다 큰 수 입니다.')
        elif randomNumber < answer:
              print(f'{answer}보다 작은 수 입니다.')
        elif randomNumber == answer:
              print(f'===정답입니다. {name} 님 {challenge} 번 만에 맞췄습니다.===')
              break
        chance -= 1

    else:
        print('1~20사이의 숫자를 입력하세요')
    

    