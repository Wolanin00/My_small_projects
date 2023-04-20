#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt", 'r') as file1:
    letter = file1.read()

with open("./Input/Names/invited_names.txt") as file:
    invited_names = file.read().split('\n')
    for name in invited_names:
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', 'w') as file2:
            file2.write(letter.replace('[name]', name))
