magic_number = 7

while True:
    play_status = input("Would you like to play? (Y/n)")

    if play_status == "n":
        break

    user_number = int(input("Guess the magic number: "))
    if user_number == magic_number:
        print("Well done. You guess correctly!")
    elif user_number - magic_number in {1, -1}:
        print("You were off by 1")
    else:
        print("You guessed wrong. Unlucky!")