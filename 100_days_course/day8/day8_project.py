import string


def encrypt(text_encrypt, shift_encrypt):
    out = ''
    for letter in text_encrypt:
        if letter in list(string.ascii_lowercase):
            index_of_letter = list(string.ascii_lowercase).index(letter)
            index_of_letter += shift_encrypt
            if index_of_letter > 25:
                index_of_letter -= 26
            out += str((list(string.ascii_lowercase))[index_of_letter])
        else:
            out += letter
    return out


def decrypt(text_decrypt, shift_decrypt):
    out = ''
    for letter in text_decrypt:
        if letter in list(string.ascii_lowercase):
            index_of_letter = list(string.ascii_lowercase).index(letter)
            index_of_letter -= shift_decrypt
            if index_of_letter < 0:
                index_of_letter += 26
            out += str((list(string.ascii_lowercase))[index_of_letter])
        else:
            out += letter
    return out


print("""
                           _      
                          | |     
   ___ _ __   ___ ___   __| | ___ 
  / _ \ '_ \ / __/ _ \ / _` |/ _ \ 
 |  __/ | | | (_| (_) | (_| |  __/
  \___|_| |_|\___\___/ \__,_|\___|
      _                    _      
     | |                  | |     
   __| | ___  ___ ___   __| | ___ 
  / _` |/ _ \/ __/ _ \ / _` |/ _ \ 
 | (_| |  __/ (_| (_) | (_| |  __/
  \__,_|\___|\___\___/ \__,_|\___|
 """)
if_play_again = True
while if_play_again:
    choice = ''
    is_correct_choice = False
    while not is_correct_choice:
        choice = input('Type "encode" to encrypt, type "decode" to decrypt >>> ').lower()
        if choice in ["encode", "decode"]:
            is_correct_choice = True
    text = input("Type your message >>> ").lower()
    shift = int(input("Type the shift number >>> "))
    shift = shift % 26

    if choice == 'encode':
        encrypt_text = encrypt(text_encrypt=text, shift_encrypt=shift)
        print(f'Your encode text is: {encrypt_text}')
    elif choice == 'decode':
        decrypt_text = decrypt(text_decrypt=text, shift_decrypt=shift)
        print(f'Your decode text is: {decrypt_text}')
    choice_play_again = input('Would you like to try again? [Yes, No] >>> ').lower()
    if choice_play_again == 'yes':
        if_play_again = True
    else:
        if_play_again = False
