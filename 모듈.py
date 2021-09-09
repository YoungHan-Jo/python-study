import random
import my_module as my

random_side = random.randint(0,1)

if random_side == 1:
    print('앞면')
else:
    print('뒷면')

print(my.pi)