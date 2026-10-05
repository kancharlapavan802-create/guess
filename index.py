import random


def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number > 0:
                return number

            print("Please enter a positive number.")

        except ValueError:
            print("Please enter a valid number.")


def play_game():
    print("\n========== NUMBER GUESSING GAME ==========")

    maximum = get_number(
        "Enter the maximum number for the game: "
    )

    secret_number = random.randint(1, maximum)

    # Number of attempts based on the size of the range
    attempts_limit = max(5, maximum.bit_length() * 2)

    attempts = 0
    score = 100

    print(f"\nI selected a number between 1 and {maximum}.")
    print(f"You have {attempts_limit} attempts.")

    while attempts < attempts_limit:

        guess = get_number("Enter your guess: ")
        attempts += 1

        if guess == secret_number:

            bonus = (attempts_limit - attempts) * 5
            score += bonus

            print("\n🎉 Congratulations!")
            print(f"You found the number in {attempts} attempts.")
            print(f"Your score: {score}")
            return

        elif guess < secret_number:
            print("📈 Too low!")

        else:
            print("📉 Too high!")

        remaining = attempts_limit - attempts

        print(f"Attempts remaining: {remaining}")

    print("\n❌ Game Over!")
    print(f"The correct number was: {secret_number}")


while True:

    play_game()

    choice = input("\nDo you want to play again? (yes/no): ")

    if choice.lower() != "yes":
        print("\nThanks for playing! 👋")
        break