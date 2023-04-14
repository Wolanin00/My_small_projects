import random


def create_character_name():
    return input("Choose your name for your character >>> ")


class Person:
    def __init__(self):
        self.hp = random.randint(80, 120)
        self.attack = random.randint(3, 6)
        self.name = create_character_name()
        self.money = 0

    def attack_monster_and_get_monster_hp(self, monster):
        monster.hp -= self.attack
        return monster.hp


class Monster:
    def __init__(self):
        self.hp = random.randint(20, 30)
        self.attack = random.randint(1, 3)

    def attack_person_and_get_person_hp(self, person):
        person.hp -= self.attack
        return person.hp


class MonsterBoss:
    def __init__(self):
        self.hp = random.randint(80, 120)
        self.attack = random.randint(3, 8)

    def attack_person_and_get_person_hp(self, person):
        person.hp -= self.attack
        return person.hp


if __name__ == '__main__':
    print('Welcome in MatiS RPG game :3')
    character1 = Person()
    print(f'Your character {character1.name} has {character1.hp} hp and {character1.attack} attack power')
    print(f'You are walking through the forest and you meet a monster')
    monster1 = Monster()
    print(f'Monster has {monster1.hp} hp and {monster1.attack} attack power')
    a = True
    choice = input('Do you fight with them? [Y, N]').lower()
    while a:
        if choice in ['y', 'n']:
            a = False
        else:
            print('Wrong answer. Pls write again')
            choice = input('Do you fight with them? [Y, N]').lower()
    if choice == 'y':
        let = True
        while let:
            print(f'You dealt damage of magnitude {character1.attack}')
            character1.attack_monster_and_get_monster_hp(monster1)
            if monster1.hp <= 0:
                print('You killed monster')
                let = False
                benefit = input("""
Choose your benefit:
[1] + 5 dmg
[2] + 30 hp
>>> """)
                c = True
                while c:
                    if benefit in ['1', '2']:
                        c = False
                    else:
                        print('Wrong answer. Pls write again')
                        benefit = input("""
Choose your benefit:
[1] + 5 dmg
[2] + 30 hp
>>> """)
                if benefit == '1':
                    character1.attack += 5
                elif benefit == '2':
                    character1.hp += 30
            else:
                print(f'Monster has {monster1.hp} hp')
                print(f'Monster gave you {monster1.attack} damage')
                monster1.attack_person_and_get_person_hp(character1)
                if character1.hp <= 0:
                    print('You dead')
                else:
                    print(f'You have {character1.hp} hp')
                    b = True
                    choice1 = input('Want to keep fighting? [Y, N] >>> ').lower()
                    while b:
                        if choice1 in ['y', 'n']:
                            b = False
                        else:
                            print('Wrong answer. Pls write again')
                            choice1 = input('Want to keep fighting? [Y, N] >>> ')
                    if choice1 == 'n':
                        let = False
                        lose_hp = random.randint(10, 20)
                        print(f'You\'re a coward and you lose {lose_hp} hp')
                        character1.hp -= lose_hp
    elif choice == 'n':
        lose_hp = random.randint(10, 20)
        print(f'You\'re a coward and you lose {lose_hp} hp')
        character1.hp -= lose_hp

    print(f'Your character {character1.name} has {character1.hp} hp and {character1.attack} attack power')
    choice2 = input('In the forest you see a fork in the road. Are you going right or left? [R, L]').lower()
    a = True
    while a:
        if choice2 in ['r', 'l']:
            a = False
        else:
            print('Wrong answer. Pls write again')
            choice2 = input('In the forest you see a fork in the road. Are you going right or left? [R, L]').lower()
    if choice2 == 'r':
        print('You found a MONSTER Grrrr')
        monster_boss = MonsterBoss()
        print(f'Monster has {monster_boss.hp} hp and {monster_boss.attack} attack power')
        a = True
        choice = input('Do you fight with them? [Y, N]').lower()
        while a:
            if choice in ['y', 'n']:
                a = False
            else:
                print('Wrong answer. Pls write again')
                choice = input('Do you fight with them? [Y, N]').lower()
        if choice == 'y':
            let = True
            while let:
                print(f'You dealt damage of magnitude {character1.attack}')
                character1.attack_monster_and_get_monster_hp(monster_boss)
                if monster_boss.hp <= 0:
                    print('You killed monster')
                    let = False
                    benefit = input("""
Choose your benefit:
[1] + 5 dmg
[2] + 30 hp
>>> """)
                    c = True
                    while c:
                        if benefit in ['1', '2']:
                            c = False
                        else:
                            print('Wrong answer. Pls write again')
                            benefit = input("""
Choose your benefit:
[1] + 5 dmg
[2] + 30 hp
>>> """)
                    if benefit == '1':
                        character1.attack += 5
                    elif benefit == '2':
                        character1.hp += 30
                else:
                    print(f'Monster has {monster_boss.hp} hp')
                    print(f'Monster gave you {monster_boss.attack} damage')
                    monster_boss.attack_person_and_get_person_hp(character1)
                    if character1.hp <= 0:
                        print('You dead')
                    else:
                        print(f'You have {character1.hp} hp')
                        b = True
                        choice1 = input('Want to keep fighting? [Y, N] >>> ').lower()
                        while b:
                            if choice1 in ['y', 'n']:
                                b = False
                            else:
                                print('Wrong answer. Pls write again')
                                choice1 = input('Want to keep fighting? [Y, N] >>> ')
                        if choice1 == 'n':
                            let = False
                            lose_hp = random.randint(10, 20)
                            print(f'You\'re a coward and you lose {lose_hp} hp')
                            character1.hp -= lose_hp
        elif choice == 'n':
            lose_hp = random.randint(10, 20)
            print(f'You\'re a coward and you lose {lose_hp} hp')
            character1.hp -= lose_hp
    elif choice2 == 'l':
        print('You meet a monster')
        monster2 = Monster()
        print(f'Monster has {monster2.hp} hp and {monster2.attack} attack power')
        a = True
        choice = input('Do you fight with them? [Y, N]').lower()
        while a:
            if choice in ['y', 'n']:
                a = False
            else:
                print('Wrong answer. Pls write again')
                choice = input('Do you fight with them? [Y, N]').lower()
        if choice == 'y':
            let = True
            while let:
                print(f'You dealt damage of magnitude {character1.attack}')
                character1.attack_monster_and_get_monster_hp(monster2)
                if monster2.hp <= 0:
                    print('You killed monster')
                    let = False
                    benefit = input("""
Choose your benefit:
[1] + 5 dmg
[2] + 30 hp
>>> """)
                    c = True
                    while c:
                        if benefit in ['1', '2']:
                            c = False
                        else:
                            print('Wrong answer. Pls write again')
                            benefit = input("""
Choose your benefit:
[1] + 5 dmg
[2] + 30 hp
>>> """)
                    if benefit == '1':
                        character1.attack += 5
                    elif benefit == '2':
                        character1.hp += 30
                else:
                    print(f'Monster has {monster2.hp} hp')
                    print(f'Monster gave you {monster2.attack} damage')
                    monster2.attack_person_and_get_person_hp(character1)
                    if character1.hp <= 0:
                        print('You dead')
                    else:
                        print(f'You have {character1.hp} hp')
                        b = True
                        choice1 = input('Want to keep fighting? [Y, N] >>> ').lower()
                        while b:
                            if choice1 in ['y', 'n']:
                                b = False
                            else:
                                print('Wrong answer. Pls write again')
                                choice1 = input('Want to keep fighting? [Y, N] >>> ')
                        if choice1 == 'n':
                            let = False
                            lose_hp = random.randint(10, 20)
                            print(f'You\'re a coward and you lose {lose_hp} hp')
                            character1.hp -= lose_hp
        elif choice == 'n':
            lose_hp = random.randint(10, 20)
            print(f'You\'re a coward and you lose {lose_hp} hp')
            character1.hp -= lose_hp

    print(f'Your character {character1.name} has {character1.hp} hp and {character1.attack} attack power')
    print('You won')
    print('''
     ___________
    '._==_==_=_.'
    .-\:      /-.
   | (|:.     |) |
    '-|:.     |-'
      \::.    /
       '::. .'
         ) (
       _.' '._
      `"""""""`
''')

