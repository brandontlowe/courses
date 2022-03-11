magic_number = 7
play_status = input("Enter 'y' to play the magic number game: ").lower()

if play_status == "y":
    user_number = int(input("Guess the magic number: "))
    if user_number == magic_number:
        print("Well done. You guess correctly!")
    elif user_number - magic_number in {1, -1}:
        print("You were off by 1")
    else:
        print("You guessed wrong. Unlucky!")