import random

choices = {
    1: """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
    2: """    _______
---'    ____)____
          ______)
         _______)
        _______)
---.__________)""",
    3: """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""}

print('Welcome in game "Rock Paper Scissors"')
my_choice = input("""What is your sign?
[1] Rock
[2] Paper
[3] Scissors
>>> """)
while my_choice not in ['1', '2', '3']:
    print('Wrong sign, Pls enter again ')
    my_choice = input("""[1] Rock
[2] Paper
[3] Scissors
>>> """)
my_choice_int = int(my_choice)
computer_choice = random.randint(1, 3)
print(choices[my_choice_int])
print('Computer choice')
print(choices[computer_choice])
if my_choice_int == computer_choice:
    print("It is a draw!")
elif my_choice_int == 3 and computer_choice == 1:
    print('Computer win!')
elif my_choice_int == 1 and computer_choice == 3:
    print('You win!')
elif my_choice_int > computer_choice:
    print("You win!")
else:
    print('Computer win!')


