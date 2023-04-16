def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2


logo = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
print(logo)

operation = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}


def calculator():
    first_number = float(input("What's the first number?: "))
    for symbols in operation:
        print(symbols)
    is_continue_calculating = True
    while is_continue_calculating:
        operation_symbol = input("Pick an operation: ")
        next_number = float(input("What's the next number?: "))
        calculation_function = operation[operation_symbol]
        result = calculation_function(first_number, next_number)
        print(f'{first_number} {operation_symbol} {next_number} = {result}')
        continue_calculating = input(f"Type 'y' to continue calculating with {result}, "
                                     f"or type 'n' to start a new calculation"
                                     f"or type 'e' to exit: ")
        if continue_calculating == 'y':
            first_number = result
        elif continue_calculating == 'n':
            is_continue_calculating = False
            calculator()
        else:
            break


calculator()
