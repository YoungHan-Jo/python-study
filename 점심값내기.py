import random

# π¨ μ¬κΈ°λ κ·Έλλ‘ π
names_string = input("λ΄κΈ°λ₯Ό ν  μΉκ΅¬λ€μ μ΄λ¦μ μ μ΅λλ€. μ½€λ§(,)λ‘ λΆλ¦¬ν΄μ μ μ΅λλ€.\n")
names = names_string.split(",")
# π¨ μ¬κΈ°λ κ·Έλλ‘ π

#μλμ μ½λ μμ± π
randIndex = random.randint(0,len(names)-1)
print(f'μ€λμ μ μ¬μ {names[randIndex]} λμ΄ μ©λλ€.')
