import random

cards = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'j': 10,
    'q': 10,
    'k': 10,
    'as': 11,
}
logo = """
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
                       _/ |                
                      |__/                 """


def who_is_win(name: str):
    print(f'{name} wins!'.capitalize())


def cards_value(cards):
    return [card[1] for card in cards]


def sum_cards(cards):
    return sum([card[1] for card in cards])


def is_play_blackjack():
    choice = input("Do you want to play a game of BackJack? ['y' or 'n'] >>> ")
    if choice == 'y':
        play_black_jack()
    else:
        exit()


def if_player_keep_drawing_cards():
    choice = input("Do you want to keep next card? ['y' or 'n'] >>> ")
    if choice == 'y':
        return True
    else:
        return False


def if_croupier_keep_drawing_cards(cards):
    if sum_cards(cards) < 17:
        return True
    else:
        return False


def play_black_jack():
    croupier = [random.choice(list(cards.items())), random.choice(list(cards.items()))]
    # croupier = [('as', 11), ('10', 10)]
    player = [random.choice(list(cards.items())), random.choice(list(cards.items()))]
    # player = [('as', 11), ('10', 10)]

    if sum_cards(player) > 21:
        player[0] = ('1', 1)

    print(f"Your cards is {cards_value(player)} with sum = {sum_cards(player)}")
    print(f"Croupier card is {cards_value(croupier)[0]}")

    player_keep_drawing = if_player_keep_drawing_cards()

    while player_keep_drawing:
        player.append(random.choice(list(cards.items())))
        print(f"Your cards is {cards_value(player)} with sum = {sum_cards(player)}")
        if sum_cards(player) > 21 and sum_cards(croupier) == 21:
            print('You loose, Croupier has BlackJack')
            player_keep_drawing = False
            print('\n')
            is_play_blackjack()
        if sum_cards(player) > 21:
            who_is_win('croupier')
            player_keep_drawing = False
            print('\n')
            is_play_blackjack()
        player_keep_drawing = if_player_keep_drawing_cards()

    croupier_keep_drawing = if_croupier_keep_drawing_cards(croupier)
    while croupier_keep_drawing:
        croupier.append(random.choice(list(cards.items())))
        croupier_keep_drawing = if_croupier_keep_drawing_cards(croupier)

    print(f"Final Player cards is {cards_value(player)} with sum = {sum_cards(player)}")
    print(f"Final Croupier card is {cards_value(croupier)} with sum = {sum_cards(croupier)}")

    if sum_cards(player) == sum_cards(croupier):
        print("It is a draw!")
    elif sum_cards(croupier) == 21:
        print('You loose, Croupier has BlackJack')
    elif sum_cards(player) == 21:
        print('You win, You has BlackJack')
    elif sum_cards(croupier) > 21:
        who_is_win('you')
    elif sum_cards(player) > sum_cards(croupier):
        who_is_win('you')
    else:
        who_is_win('croupier')
    print('\n')
    is_play_blackjack()


print(logo)
is_play_blackjack()
