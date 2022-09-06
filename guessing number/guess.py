random_number = 7
guess_count = 0
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input("Guess the number:"))
    guess_count +=1
    if guess == random_number:
        print("You won!")
        break
else:
    print("Oops, sorry you lose the game")