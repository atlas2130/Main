"""
This code is for a Minigame chooser.
"""
__author__ = "Drake Willis"
import random


def main():
    """
This is the code to choose what minigame you want to play.
    """
    run = True
    while run:
        print("Enter the Minigame you would like to see ")
        print("1: Mad Libs Game")
        print("2: Estimate Program Cost")
        print("3: Secret Number Game")
        print("4: End Program")
        user_input = input()
        try:
            option = int(user_input)
            if 1 == option:
                ad_libs_game()
            elif 2 == option:
                estimate_game()
            elif 3 == option:
                print("What difficulty would you like to play?")
                print("A: Easy")
                print("B: Hard")
                difficulty = input("Enter either A or B: ")
                if difficulty == "A":
                    secret_number_game(10)
                elif difficulty == "B":
                    secret_number_game(5)
            elif option == 4:
                run = False
                break
            elif option > 4:
                print("Invalid selection. Try again.")
        except ValueError:
            print("Invalid selection. Try again.")


def ad_libs_game():
    """
This is the code for the ad libs game which you input words to make a funny
prompt.
    """
    print("Hello and Welcome to the Crazy Mad Libs Game!")
    print(
        "Today we are doing to play a game where you are going to input 22"
        "words and see what crazy prompt you come up with!")
    print("In this story you a programmer making a funny program!")
    print("Lets get started!")
    adjective1 = input("(1)Type your adjective : ")
    name1 = input("(2)Type your name: ")
    noun1 = input("(3)Type your noun: ")
    adjective2 = input("(4)Type your adjective : ")
    plural_noun1 = input("(5)Type your plural noun: ")
    verb1 = input("(6)Type your verb : ")
    noun2 = input("(7)Type your noun: ")
    adjective3 = input("(8)Type your adjective : ")
    noun3 = input("(9)Type your noun: ")
    verb2 = input("(10)Type your verb : ")
    adjective4 = input("(11)Type your adjective : ")
    adjective5 = input("(12)Type your adjective : ")
    adverb1 = input("(13)Type your adverb: ")
    adverb2 = input("(14)Type your adverb: ")
    noun4 = input("(15)Type your noun: ")
    verb3 = input("(16)Type your verb : ")
    adverb3 = input("(17)Type your adverb: ")
    adverb4 = input("(18)Type your adverb: ")
    noun5 = input("(19)Type your noun: ")
    verb4 = input("(20)Type your verb : ")
    adjective6 = input("(21)Type your adjective : ")
    adjective7 = input("(22)Type your adjective : ")
    print("\nNow that was a lot of words!")
    print("Lets see what you came up with!")
    print("\nIt was a " + adjective1 + " day in the computer lab.",
          "A new programmer, named " + name1 + " was trying to make " + noun1 +
          " move across the screen.",
          "They had to write a " + adjective2 + " program to make it happen.")
    print(
        "\nFirst, they typed in some " + plural_noun1 + ", which are like "
                                                        "the rules for the "
                                                        "computer. They need "
                                                        "to tell the "
                                                        "computer to " +
        verb1 + " colorful " + noun2 + " and then to " + verb2 + " it to a "
                                                                 "new spot.")
    print(
        "\nBut the program had a " + adjective3 + "mistake, called a bug! "
                                                  "The " + noun3 + " didn't "
                                                                   "move. "
                                                                   "Instead, "
                                                                   "it just "
                                                                   "started "
                                                                   "to " +
        verb2 + " and made a " + adjective4 + " noise. The programmer was so "
                                              "" + adjective5 + "!")
    print(
        "\nThey looked at their code again and found a small mistake. They "
        "had told the computer to go " + adverb1 + " instead of " + adverb2
        + ". They fixed the bug, and this time, the " + noun4 + " started to "
                                                                "" + verb3 +
        " across the screen, " + adverb3 + " and " + adverb4 + ".")
    print(
        "\nEveryone cheered! The programmer had finally made the " + noun5 +
        "work. They were so happy, they decided to make it " + verb4
        + " and sing a " + adjective6 + " song. It was a funny and "
        + adjective7 + " end to a long day of coding.")
    main()


def estimate_game():
    """
This is the code for the estimate the profits and how he uses his money.
    """
    print(
        "Lets see how much money this programmer might make if he sold his "
        "program to 100 companies!")
    program_cost = float(
        input("How much money do you think this program is worth?: "))
    '''^This is when I am using numeric operators, and I am multiplying the
        amount the program is worth and the 100 companies that bought it.'''
    total_money_made = program_cost * 100
    print("He made around: $", format(float(total_money_made), ".2f"), sep="")
    half_gone = program_cost / 2.0
    mod_money = program_cost % 2
    floor_money = program_cost // 2
    print("If the number is zero the money he made was even:", mod_money)
    print("This shows the floor division of his money by two:", floor_money)
    print(
        "This is how much he made if he gave half" +
        " his money away to charity: $",
        format(float(half_gone), ".2f"), sep="")


def secret_number_game(max_guess):
    """
This is the code for the secret number game in which you try to guess a
random number with either 5 or 10 guesses.
    :param max_guess:
    The parameter max_guess is the maximum number of guesses you get when
    you try to guess the number.
    """
    secret_number = random.randint(1, 20)
    guesses_left = max_guess
    print("Welcome to the secret number game!")
    print("Try to guess the secret number between 1 and 20! You have " + str(
        guesses_left) + " guesses left.")
    for attempts in range(guesses_left):
        try:
            guess = int(input("Enter your guess: "))
            if guess not in range(1, 21):
                print("Invalid guess. Try again.")
                continue
            if guess == secret_number:
                print("You guessed the secret number!")
                main()
            if secret_number - 3 < guess < secret_number + 3:
                print("You are getting close to your secret number!")
            elif guess < 5 or guess > 15:
                print("You are far from the secret number!")
        except ValueError:
            print("Invalid guess. Try again.")
    else:
        print(
            f"\nSorry, you are out of guesses!" +
            f"The secret number was {secret_number}.")
        main()


if __name__ == "__main__":
    main()

