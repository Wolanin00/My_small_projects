import random
import logo

difficulty = {
    'easy': 10,
    'hard': 5
}


def play_again():
    again = input("Do you want to play again? ['y' or 'n'] >>> ")
    if again == 'y':
        choose_difficulty_and_play()
    else:
        exit()


def choose_difficulty_and_play():
    chosen_difficult = input(f"Chose a difficulty. {list(difficulty.keys())}: ")
    if chosen_difficult in list(difficulty.keys()):
        play_game(difficulty[chosen_difficult])
    else:
        print('Wrong choice! Try again')
        choose_difficulty_and_play()


def check_answer(try_to_guess, drawn_number, attempts):
    if try_to_guess == drawn_number:
        print("You win")
        attempts = -1
        play_again()
    elif try_to_guess > drawn_number and attempts > 1:
        print("To high, Try again lower number")
    elif try_to_guess < drawn_number and attempts > 1:
        print("To low, Try again higher number")
    attempts -= 1
    return attempts


def play_game(attempts):
    drawn_number = random.randint(1, 100)
    # print(drawn_number)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        try_to_guess = int(input("Make a guess: "))
        attempts = check_answer(try_to_guess=try_to_guess, drawn_number=drawn_number, attempts=attempts)
        if attempts == 0:
            print("You loose")
            print(f"Correct number was: {drawn_number}")
            play_again()


print(logo.guess_the_number_logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choose_difficulty_and_play()
