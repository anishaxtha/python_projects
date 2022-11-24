questions = ("What are asteroid made up of?",
                          "Which animals lays the largest eggs?",
                          "Who had coined the term asteroid?",
                          "How many bones in human body?",
                          "When NASA had launched its first mission to Sun?")

options = (("A. Minor Planets","B. Small Stars","C. Planets","D. Only A and B"),
                      ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                      ("A. Carl Sagan","B. William Herschel", "C. Issac Newton","D. Edmond Halley"),
                      ("A. 206", "B. 207", "C. 208", "D. 209"),
                      ("A. 2016","B. 2017", "C. 2018", "D. None of the above"))


answers=("D", "D", "B", "A", "C")
guesses=[]
score = 0
question_num=0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess== answers[question_num]:
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("-------------------")
print("      Results       ")
print("-------------------")


print("answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()


score = int(score/ len(questions)*100)
print(f"Your score is {score}%")











