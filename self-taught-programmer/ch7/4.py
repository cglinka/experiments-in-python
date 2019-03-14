numbers = [5, 6, 7, 8, 9, 10]

while True:
    guess = input("Guess a number in the list, or type 'q' to quit: ")
    if guess == 'q':
        break

    try:
        guess = int(guess)
    except ValueError:
        print("That's not a valid number")
        continue

    if guess in numbers:
        print("You guessed correctly!")
    else:
        print("Nope!")
