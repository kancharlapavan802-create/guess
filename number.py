import random
import os
import time


# ---------- COLORS ----------

RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"


# ---------- CLEAR SCREEN ----------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ---------- TITLE ----------

def show_title():
    print(CYAN + BOLD)
    print("=" * 55)
    print("        🎯 NUMBER GUESSING CHALLENGE")
    print("=" * 55)
    print(RESET)


# ---------- GET INTEGER ----------

def get_number(message):
    while True:
        try:
            number = int(input(message))

            if number > 0:
                return number

            print(RED + "❌ Enter a positive number!" + RESET)

        except ValueError:
            print(RED + "❌ Please enter a valid number!" + RESET)


# ---------- DIFFICULTY ----------

def choose_difficulty():

    print(YELLOW + "\nChoose Difficulty\n" + RESET)

    print("1. 🟢 Easy")
    print("2. 🟡 Medium")
    print("3. 🔴 Hard")
    print("4. 💀 Extreme")

    while True:

        choice = input("\nEnter choice (1-4): ")

        if choice == "1":
            return 1, 10

        elif choice == "2":
            return 1, 100

        elif choice == "3":
            return 1, 1000

        elif choice == "4":
            print(MAGENTA +
                  "\n💀 EXTREME MODE" +
                  RESET)

            minimum = get_number("Enter minimum number: ")
            maximum = get_number("Enter maximum number: ")

            while maximum <= minimum:
                print(RED + "Maximum must be greater than minimum!" + RESET)
                maximum = get_number("Enter maximum number: ")

            return minimum, maximum

        else:
            print(RED + "Invalid choice!" + RESET)


# ---------- HINT ----------

def give_hint(secret, guess):

    difference = abs(secret - guess)

    if difference == 0:
        return

    if difference <= 5:
        print(GREEN + "🔥 You're extremely close!" + RESET)

    elif difference <= 20:
        print(YELLOW + "✨ You're close!" + RESET)

    elif difference <= 100:
        print(BLUE + "🌊 You're getting warmer!" + RESET)

    else:
        print(MAGENTA + "❄️ You're far away!" + RESET)


# ---------- GAME ----------

def play_game(high_score):

    clear_screen()
    show_title()

    minimum, maximum = choose_difficulty()

    secret = random.randint(minimum, maximum)

    # Attempts scale with range size
    range_size = maximum - minimum + 1

    attempts = max(
        5,
        range_size.bit_length() + 3
    )

    score = 100
    streak = 0

    print(
        f"\n{CYAN}🎯 Guess a number between "
        f"{minimum} and {maximum}{RESET}"
    )

    print(
        f"{YELLOW}❤️ You have {attempts} attempts.{RESET}"
    )

    time.sleep(1)

    while attempts > 0:

        print("\n" + "-" * 45)

        guess = get_number(
            f"{CYAN}Enter your guess: {RESET}"
        )

        attempts -= 1

        if guess == secret:

            streak += 1

            bonus = attempts * 10
            score += bonus

            print(GREEN + BOLD)
            print("\n🎉🎉 YOU WON! 🎉🎉")
            print(f"🏆 Number: {secret}")
            print(f"⭐ Score: {score}")
            print(f"🔥 Streak: {streak}")
            print(RESET)

            if score > high_score:
                high_score = score

                print(
                    YELLOW +
                    "🏆 NEW HIGH SCORE!" +
                    RESET
                )

            return high_score

        elif guess < secret:

            print(
                BLUE +
                "📈 Too LOW!" +
                RESET
            )

            give_hint(secret, guess)

        else:

            print(
                RED +
                "📉 Too HIGH!" +
                RESET
            )

            give_hint(secret, guess)

        print(
            YELLOW +
            f"❤️ Attempts left: {attempts}" +
            RESET
        )

        score -= 5

    print(RED + BOLD)
    print("\n💀 GAME OVER!")
    print(f"The correct number was: {secret}")
    print(RESET)

    return high_score


# ---------- MAIN ----------

def main():

    high_score = 0

    while True:

        high_score = play_game(high_score)

        print(
            f"\n🏆 Current High Score: "
            f"{high_score}"
        )

        choice = input(
            "\n🔄 Play again? (yes/no): "
        )

        if choice.lower() != "yes":

            print(
                GREEN +
                "\nThanks for playing! 👋" +
                RESET
            )

            break


main()