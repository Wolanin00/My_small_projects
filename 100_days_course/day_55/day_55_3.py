# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        function(args[0], args[1], args[2])
    return wrapper

# Use the decorator 👇

@logging_decorator
def a_function(*args):
    suma = 0
    for i in args:
        suma += i
    print(f"It returned: {suma}")


a_function(1, 2, 3)
