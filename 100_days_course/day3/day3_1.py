def leap_year(year: int):
    if year % 4 == 0:
        if year % 100 != 0:
            print('Leap year.')
        elif year % 100 == 0 and year % 400 == 0:
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Not leap year.')


if __name__ == '__main__':

    year = int(input("Which year do you want to check? "))
    leap_year(year)
