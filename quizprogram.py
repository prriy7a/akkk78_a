from question import question_bank
from question import options
print("**************************")
print("Welcome to My Quiz Game")
score=0
def check_answer(userguess,correctanswer):
    if userguess==correctanswer:
        return True
    else:
        return False
for question in range(len(question_bank)):
    print("**********************")
    print(question_bank[question]["text"])
    for i in options[question]:
        print(i)
    guess=input("Enter your answer(A/B/C/D):").upper()
    is_correct=(check_answer(guess,question_bank[question]["answer"]))
    if is_correct:
        print("Correct Answer")
        score+=1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {question_bank[question]["answer"]}")
    print(f"Your current score is {score}/{question+1}")
print(f"Your final score is {score}")
print(f"Your score is {(score/len(question_bank))*100} %")

