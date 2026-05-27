import random


def game():
    secret = random.randint(1, 100)
    max_tries = 7
    tries = 0

    while tries < max_tries:
        try:
            guess = int(input(f"{tries+1} time guess:"))
        except:
            ValueError
            print("please enter valid intger")
            continue

        tries += 1

        if guess > secret:
            print("Guess bigger!")
        elif guess < secret:
            print("Guess smaller!")
        else:
            print(f"congrats,Guessing correctly！you spent {tries} time!")
            return

    print(f"Game over!The right answer is {secret}")


while True:
    game()
    again = input("再玩一局？(y/n):")
    if again != "y":
        print("再见！")
        break
