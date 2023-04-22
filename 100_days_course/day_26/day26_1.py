numbers = [1, 2, 3]

new_list = [item + 1 for item in numbers]

number_list = [n for n in range(1, 100)
               if n % 2 == 0
               if n % 3 == 0]
print(number_list)


