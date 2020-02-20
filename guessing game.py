# say we wanna build a game for user to guess a preset secret word
# we can use while loop for each time user guess. keep asking until user guess correctly

secret_word = "giraffe"
guess = ""    # remember to always define empty variable first for while loop

while guess != secret_word:
    guess = input("Enter guess: ")

print("You win!")    # note that this will only be executed if we break the while loop. meaning guess = secret_word


# say we wanna set a limit to the guess, say 3 tries
# we need to set variables first and the validation if user is out uf guesses
secret_word = "elephant"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):    # need to check if user can guess or not first, then only we let user guess
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1    # adding 1 tries on top of guess count, keep looping
    else:                                # loop breaks since out of guesses
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")
