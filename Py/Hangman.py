name = input("Enter Name")
print("Welcome " + name + "time to play hangman")

secret_word = "Metallica"
lives = 10
guess_string = ""
while  lives > 0:
    guess = input("Guess a letter:")
    guess_string += guess

    for character in secret_word:
        if character in guess_string:
            print(character)
        else:
            print("-")

    if set(secret_word) == set(guess_string):
        print("Very well you win.")
        break

    if guess not in secret_word:
        lives-=1
        print("Wrong guess!")
        print(f"u have {lives} left")
        if lives == 0:
            print("You Died!")




