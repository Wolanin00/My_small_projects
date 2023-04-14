print("""
                   _..
  /}_{\           /.-'
 ( a a )-.___...-'/
 ==._.==         ;
      \ i _..._ /,
      {_;/   {_//  fsc
      """)
print('Marta\'s game about cat Mrauuu')
choice1 = input("Imagine that you are a cat and you found a mouse. Will you kill a mouse? [Yes, No] >>> ").lower()
if choice1 == 'no':
    print('You have nothing to eat, you starved to death')
    print('You woke up and you have a second chance')
    choice2 = input('Will you kill the mouse now? [Yes, No] >>> ').lower()
    if choice2 == 'yes':
        print('You are a total brute. You do what you\'re told')
        print('You went to hell')
    elif choice2 == 'no':
        print('You\'re like an angel, you\'ve gone to heaven')
    else:
        print('The wrong answer')
elif choice1 == 'yes':
    print('You killed a mouse and you are murderer, but you can right now eat a mouse.')
    choice2 = input('Will you eat a mouse? [Yes, No] >>> ').lower()
    if choice2 == 'yes':
        print('You are happy cause you are not hungry right now')
    elif choice2 == 'no':
        print('In addition to being a murderer, you will starve to death yourself.')
        print('You went to hell')
    else:
        print('The wrong answer')
else:
    print('The wrong answer')
