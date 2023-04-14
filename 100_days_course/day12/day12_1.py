numer = 1
numer2 = 1


def increment():
    global numer, numer2
    numer += 1
    numer2 += 2
    print(numer, numer2, sep='   ')


increment()
print(numer, numer2, sep='   ')
