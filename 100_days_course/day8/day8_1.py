import string

def greet(how_many_times: int = 1):
    for _ in range(how_many_times):
        print('one', 'two', 'three', sep='\n')


greet(2)
for i in range(1, 4, -1):
    print('i')

print(len(list(string.ascii_lowercase)))
print((list(string.ascii_lowercase))[25])
