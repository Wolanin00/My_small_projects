print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? $'))
amount_of_people = int(input('How many people to split the bill? -> '))
tip_percentage = int(input('What percentage tip would you like to give? 0, 10, 12, or 15? -> '))
if tip_percentage not in [0, 10, 12, 15]:
    print('This percentage is not valid with the values provided')
    exit()
total_play_with_tip = total_bill*(1+(tip_percentage/100))
amount_per_person = total_play_with_tip/amount_of_people

print('Each person should pay: $', round(amount_per_person, 2))
