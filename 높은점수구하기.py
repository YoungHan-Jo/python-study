# π¨ μ¬κΈ°λ κ·Έλλ‘ π
student_scores = input("νμλ€μ μ±μ μ μλ ₯ :\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  #μ±μ  μλ ₯μ λ¬Έμμ΄λ‘ λ°κΈ° λλ¬Έμ λ€μ μ μλ‘ λ³νν΄μ λ¦¬μ€νΈμ μλ ₯
print(student_scores)
# π¨ μ¬κΈ°λ κ·Έλλ‘ π

# μλμ μ½λ μμ± π
highest_score = 0

for score in student_scores:
    if highest_score < score:
        highest_score = score

    
print(f"κ°μ₯ λμ μ μλ : {highest_score}")