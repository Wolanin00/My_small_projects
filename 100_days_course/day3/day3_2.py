def true_love(name1: str, name2: str):
    both_name = name1.lower() + name2.lower()
    first_number = both_name.count('t') + both_name.count('r') + both_name.count('u') + both_name.count('e')
    second_number = both_name.count('l') + both_name.count('o') + both_name.count('v') + both_name.count('e')
    number = int(str(first_number) + str(second_number))
    if number < 10 or number > 90:
        print(f'Your score is {number}, you go together like coke and mentos.')
    elif 40 <= number <= 50:
        print(f'Your score is {number}, you are alright together.')
    else:
        print(f'Your score is {number}.')


if __name__ == '__main__':
    print("Welcome to the Love Calculator!")
    first_name = input("What is your name? \n")
    second_name = input("What is their name? \n")
    true_love(first_name, second_name)
