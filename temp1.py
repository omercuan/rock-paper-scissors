import random

while True:
    try:
        users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
        if users_choice not in [0, 1, 2]:
            print("Invalid choice, please choose 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input, please enter a number (0, 1, or 2).")
        continue

    choices = [
        """
        ROCK:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        """,
        """
        PAPER:
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
        """,
        """
        SCISSORS:
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        """
    ]

    print(choices[users_choice])

    print("Computer chose:")
    random_number = random.randint(0, 2)
    print(choices[random_number])

    if users_choice == random_number:
        print("DRAW")
    elif (users_choice == 0 and random_number == 2) or \
         (users_choice == 1 and random_number == 0) or \
         (users_choice == 2 and random_number == 1):
        print("YOU WIN")
        break
    else:
        print("YOU LOSE")
        break
