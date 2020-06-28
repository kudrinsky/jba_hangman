import random
print('H A N G M A N')
words = ('python', 'java', 'kotlin', 'javascript')
ai_choice = random.choice(words)
current_state = ['-' for i in range(len(ai_choice))]


def game():
    menu_item = None
    while menu_item not in ('play', 'exit'):
        menu_item = input('Type "play" to play the game, "exit" to quit:')
        if menu_item == 'exit':
            pass
        elif menu_item == 'play':
            main_loop()


def update_word(char):
    global current_state
    for i in range(len(ai_choice)):
        if ai_choice[i] == char:
            current_state[i] = char


def main_loop():
    lives = 8
    input_history = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while lives > 0:
        print('\n' + ''.join(current_state))
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('You should input a single letter')
        elif letter not in alphabet:
            print('It is not an ASCII lowercase letter')
        elif letter not in input_history:
            input_history.append(letter)
            if letter not in set(ai_choice):
                print('No such letter in the word')
                lives -= 1
            else:
                update_word(letter)
                if ai_choice == ''.join(current_state):
                    print(f'You guessed the word {ai_choice}!\nYou survived!')
                    break
        else:
            print('You already typed this letter')
    else:
        print('You are hanged!')
    print()
    game()


game()
