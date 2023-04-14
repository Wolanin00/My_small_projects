import replit
from replit import clear

logo = """
                         ___________
                         \         /
                          )_______(
                          |       |_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )       (
                         /_________\ 
                         `'-------'`
                       .-------------.
                      /_______________\ 
"""

print(logo)
print("Welcome to the secret auction program.")
is_auctions_more = True
all_bidders = {}
while is_auctions_more:
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: $"))
    all_bidders[name] = bid
    auctions_more = input("Are there any other bidders? Type 'yes' or 'no' >>> ").lower()
    if auctions_more != 'yes':
        is_auctions_more = False
    else:
        replit.clear()

sorted_all_bidders = sorted(all_bidders.items(), key=lambda x: x[1], reverse=True)
print(f'The winner is {sorted_all_bidders[0][0]} with a bid of ${sorted_all_bidders[0][1]}')
