secret_word = "amazedly"
guess = ""
guess_count = 0
guess_limit = 4
guesses_limit_reached = False

while guess != secret_word and not(guesses_limit_reached):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        guesses_limit_reached = True
if guesses_limit_reached:
    print("You lose")
else:
    print("Congratulations, you win!")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

