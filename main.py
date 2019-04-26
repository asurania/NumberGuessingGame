import random



guess_list = []
guess = None
highscore = 0

def number_game():
    import random
    global guess
    global guess_list
    global play
    global highscore
    random_number = (random.randint(1, 10))

    while play.upper() == "Y":

        try:
            guess = int(input("{} What is your Guess, Pick a Number 1 to 10:  ".format(name)))

            if guess > 10 or guess < 1:
                raise ValueError("There has been an ERROR. {} the Number you have choosen is NOT between 1 and 10".format(name))

            if guess == random_number:
                print("You win")
                guess_list.append(guess)
                print("This is your {} attempt".format(len(guess_list)))

                if highscore > len(guess_list) or highscore == 0:
                    highscore = int(len(guess_list))

                    guess_list = []
                    guess = None
                print("The highscore is {}".format(highscore))
                play = input("{} Do you want to Play the Number Game Again. Y to play again:  ".format(name))
                random_number = (random.randint(1, 10))

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
    print ("Have a nice day")

print("Welcome to The Number Guessing Game")
name = input("What is your Name: ")
play = input("{} Do you want to Play the Number Game. Press Y to play:  ".format(name))
number_game()