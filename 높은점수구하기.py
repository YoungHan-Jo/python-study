# 🚨 여기는 그대로 👇
student_scores = input("학생들의 성적을 입력 :\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  #성적 입력을 문자열로 받기 때문에 다시 정수로 변환해서 리스트에 입력
print(student_scores)
# 🚨 여기는 그대로 👆

# 아래에 코드 작성 👇
highest_score = 0

for score in student_scores:
    if highest_score < score:
        highest_score = score

    
print(f"가장 높은 점수는 : {highest_score}")