import numpy as np


def if_palindrome(input_str):
    sorted_str = sorted(input_str.lower())
    len_str = len(sorted_str)
    len_str_unique = len(np.unique(sorted_str))
    if len_str == 1:
        return True
    elif len_str_unique == 1:
        return True
    elif (len_str - len_str_unique) == 0:
        return False
    elif (len_str - len_str_unique) % 2 == 0 and len_str % 2 == 0:
        return False
    elif (len_str - len_str_unique) % 2 == 0 and len_str % 2 == 1:
        if len_str_unique % 2 == 0:
            return False
        else:
            return True
    elif (len_str - len_str_unique) % 2 == 1:
        if len_str_unique % 2 == 0:
            return True
        else:
            return False
    else:
        return True


if __name__ == '__main__':
    text = ''
    while text != 'e':
        text = input('Wpisz slowo: ')
        print(if_palindrome(text))
