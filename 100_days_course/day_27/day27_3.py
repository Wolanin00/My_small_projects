def add(*m):
    result = 0
    for item in m:
        result += item
    return result


print(add(1, 2, 3, 4, 5, 6))


def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)



calculate(add=3, multiply=5)
