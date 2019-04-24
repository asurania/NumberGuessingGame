import random

random_number = (random.randint(1, 10))
print(random_number)
guess_list = []
guess = None

def number_game():
    print(random_number)
    global guess
    global guess_list
    highscore = 0
    play = input("{} Do you want to Play the Number Game. Y or N".format(name))

    while play == "Y":
        while guess != random_number:

            try:
                guess = int(input("{} What is your Guess, Pick a Number 1 to 10:  ".format(name)))

                if guess > 10 or guess < 1:
                    raise ValueError(
                        "There has been an ERROR. {} the Number you have choosen is NOT between 1 and 10".format(name))

                if guess == random_number:
                    print("You win")

                    guess_list.append(guess)
                    print("This is your {} attempt".format(len(guess_list)))

                    if highscore > len(guess_list) or highscore == 0:
                        highscore = int(len(guess_list))
                        print("The highscore is {}".format(highscore))
                        return True

                elif guess > random_number:
                    print("The value is to high {}".format(name))
                    guess_list.append(guess)
                    print("This is your {} attempt".format(len(guess_list)))
                elif guess < random_number:
                    print("The value is to low {}".format(name))
                    guess_list.append(guess)
                    print("This is your {} attempt".format(len(guess_list)))
            except ValueError as err:
                print("{} There has been an Error. You have not entered a number betwen 1 and 10".format(name))


print("Welcome to The Number Guessing Game")
name = input("What is your Name: ")
number_game()