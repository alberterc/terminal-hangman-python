import random
import time
import msvcrt
from os import system
from collections import Counter

#variable initializations
def init_hangman_game():
    global list_of_words
    global current_active_word
    global counts_of_chars
    global full_correct_word
    global wrong_letter_count
    global already_guessed_letter
    global guessed_letter
    global score
    global length_of_chosen_word
    global display_word
    global mistakes_limit
    
    with open('hangman words.txt', 'r') as file:
        file_data = file.read()
        list_of_words = list(map(str, file_data.split()))

    current_active_word = random.choice(list_of_words)
    counts_of_chars = Counter(current_active_word)
    full_correct_word = current_active_word
    wrong_letter_count = 0
    already_guessed_letter = []
    guessed_letter = ''
    score = 0
    length_of_chosen_word = len(current_active_word)
    display_word = '_' * length_of_chosen_word
    mistakes_limit = 6

#loading screen before game starts
def loading_screen():
    system('cls')
    print('=========================\n'
          '=========HANGMAN=========\n'
          '=========================\n'
          '========Loading..========\n'
          '====                 ====\n'
          '=========================')
    time.sleep(2)
    system('cls')
    print('=========================\n'
          '=========HANGMAN=========\n'
          '=========================\n'
          '========Loading..========\n'
          '====$$$              ====\n'
          '=========================')
    time.sleep(1)
    system('cls')
    print('=========================\n'
          '=========HANGMAN=========\n'
          '=========================\n'
          '========Loading..========\n'
          '====$$$$$$$$$        ====\n'
          '=========================')
    time.sleep(2)
    system('cls')
    print('=========================\n'
          '=========HANGMAN=========\n'
          '=========================\n'
          '========Loading..========\n'
          '====$$$$$$$$$$$$$$   ====\n'
          '=========================')
    time.sleep(1)
    system('cls')
    print('=========================\n'
          '=========HANGMAN=========\n'
          '=========================\n'
          '========Loading..========\n'
          '====$$$$$$$$$$$$$$$$ ====\n'
          '=========================')
    time.sleep(1)
    system('cls')
    print('=========================\n'
          '=========HANGMAN=========\n'
          '=========================\n'
          '========Loading..========\n'
          '====$$$$$$$$$$$$$$$$$====\n'
          '=========================')
    time.sleep(1)
    system('cls')
    print('=========================\n'
          '=========HANGMAN=========\n'
          '=========================\n'
          '==========READY==========\n'
          '====$$$$$$$$$$$$$$$$$====\n'
          '=========================')
    time.sleep(2)
    system('cls')

#start screen
def start_screen_hangman():
    system('cls')

    init_hangman_game()

    #start screen
    print('=========================\n'
          '=========HANGMAN=========\n'
          '=========================\n'
          '===Press Enter to play===\n'
          '====Press Esc to quit====\n'
          '=========================')
    
    #detects key presses
    key_pressed = ''
    while True:
        if msvcrt.kbhit() != 0:
            key_pressed = msvcrt.getch()
            key_pressed = key_pressed.decode()
            break
    #detects Enter key
    if key_pressed == '\r' or key_pressed == '\n':
        #loading screen
        loading_screen()
        main_hangman()
    #detects Escacpe key
    elif key_pressed == chr(27):
        exit()
    #invalid inputs
    else:
        print('\nInvalid Input\n')
        system('pause')
        system('cls')
        start_screen_hangman()

#main game
def main_hangman():
    #clears the screen
    system('cls')

    #inits
    global wrong_letter_count
    global display_word
    global current_active_word
    i = 1
    j = 1
    key_pressed = ''
    
    #prints the hangman
    if wrong_letter_count == 0:
        print('=========================\n'
                '======             ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======  __|__      ======\n'
                '=========================\n'
                '=========================\n'
                '====Press Esc to quit====\n'
                '=========================')
        print(f'{mistakes_limit - wrong_letter_count} guesses remaining.')
    elif wrong_letter_count == 1:
        print('=========================\n'
                '======     _____   ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======  __|__      ======\n'
                '=========================\n'
                '=========================\n'
                '====Press Esc to quit====\n'
                '=========================')
        print('Wrong guess! ', end = '', flush = True)
        print(f'{mistakes_limit - wrong_letter_count} guesses remaining.')
    elif wrong_letter_count == 2:
        print('=========================\n'
                '======     _____   ======\n'
                '======    |     |  ======\n'
                '======    |     |  ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======  __|__      ======\n'
                '=========================\n'
                '=========================\n'
                '====Press Esc to quit====\n'
                '=========================')
        print('Wrong guess! ', end = '', flush = True)
        print(f'{mistakes_limit - wrong_letter_count} guesses remaining.')
    elif wrong_letter_count == 3:
        print('=========================\n'
                '======     _____   ======\n'
                '======    |     |  ======\n'
                '======    |     |  ======\n'
                '======    |     O  ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======  __|__      ======\n'
                '=========================\n'
                '=========================\n'
                '====Press Esc to quit====\n'
                '=========================')
        print('Wrong guess! ', end = '', flush = True)
        print(f'{mistakes_limit - wrong_letter_count} guesses remaining.')
    elif wrong_letter_count == 4:
        print('=========================\n'
                '======     _____   ======\n'
                '======    |     |  ======\n'
                '======    |     |  ======\n'
                '======    |     O  ======\n'
                '======    |    /|\ ======\n'
                '======    |        ======\n'
                '======    |        ======\n'
                '======  __|__      ======\n'
                '=========================\n'
                '=========================\n'
                '====Press Esc to quit====\n'
                '=========================')
        print('Wrong guess! ', end = '', flush = True)
        print(f'{mistakes_limit - wrong_letter_count} guesses remaining.')
    elif wrong_letter_count == 5:
        print('=========================\n'
                '======     _____   ======\n'
                '======    |     |  ======\n'
                '======    |     |  ======\n'
                '======    |     O  ======\n'
                '======    |    /|\ ======\n'
                '======    |    /   ======\n'
                '======    |        ======\n'
                '======  __|__      ======\n'
                '=========================\n'
                '=========================\n'
                '====Press Esc to quit====\n'
                '=========================')
        print('Wrong guess! ', end = '', flush = True)
        print(f'{mistakes_limit - wrong_letter_count} guess remaining.')
    elif wrong_letter_count == 6:
        print('=========================\n'
                '======     _____   ======\n'
                '======    |     |  ======\n'
                '======    |     |  ======\n'
                '======    |     O  ======\n'
                '======    |    /|\ ======\n'
                '======    |    / \ ======\n'
                '======    |        ======\n'
                '======  __|__      ======\n'
                '=========================\n'
                '=========================\n'
                '=========================')
        print('Wrong guess! ', end = '', flush = True)
        print("You don't have anymore guesses.")
        print(f'Your guessed word was {display_word}.')
        print(f'The word was {full_correct_word}.')
        print(f"You have been hung!\n")
        system('pause')
        start_screen_hangman()

    print('=========================\n'
            + 'Word: ' + display_word +
            '\n=========================')
    # print(current_active_word)
    print('Guess a letter: ', end = '', flush = True)

    #get key presses
    while i == 1:
        if msvcrt.kbhit() != 0:
            key_pressed = msvcrt.getch()
            key_pressed = key_pressed.decode() 
            i = 0

    #if Escape key is pressed then quit the program
    if key_pressed == chr(27):
        exit()
    #if any other key is pressed, prints that key, and wait for another key press for Enter key
    elif key_pressed == '\r' or key_pressed == '\n':
        pass
    #if any other key is pressed, prints that key, and wait for another key press for Enter key 
    else:
        i = 1
        guessed_letter = key_pressed
        print(guessed_letter, end = '', flush = True)
        j = 0
        #wait the second key press
        while True:
            if msvcrt.kbhit() != 0:
                key_pressed = msvcrt.getch()
                key_pressed = key_pressed.decode() 
                break


    #when the user presses enter
    if (key_pressed == '\r' or key_pressed == '\n') and j == 0:
        i = 1
        printed = 0
        guessed_letter = guessed_letter.upper()
        
        #if the answer input isn't valid
        if len(guessed_letter) == 0 or len(guessed_letter) >= 2 or guessed_letter.isdigit():
            print('\nInvalid Answer, please only use 1 letter for each input!\n')
            system('pause')
        
        #if the answer input in the current active word
        #removes the correct guessed letter from the current active word
        elif guessed_letter in current_active_word:
            already_guessed_letter.extend([guessed_letter])
            #for every character occurrences in the current active word
            amount = counts_of_chars[guessed_letter]
            while amount != 0:
                found_in_index = current_active_word.find(guessed_letter)
                current_active_word = current_active_word[:found_in_index] + '_' + current_active_word[found_in_index + 1:]
                display_word = display_word[:found_in_index] + guessed_letter + display_word[found_in_index + 1:]
                amount -= 1
        
        #if the answer input has already been guessed before
        elif guessed_letter in already_guessed_letter:
            print('\nThis letter has already been guessed. Try again!\n')
            system('pause')
        
        #if the answer input is not in the current active word
        else:
            already_guessed_letter.extend([guessed_letter])
            wrong_letter_count += 1
    


    #check if all the letters are guessed correctly
    if current_active_word == '_' * length_of_chosen_word:
        system('cls')
        print("\nCongratulations! You've guessed the word correctly without dying!")
        print('=========================\n'
                + 'Word: ' + display_word + '\n' +
                '=========================\n')
        system('pause')
        start_screen_hangman()

    #loops the function for game continuation
    main_hangman()

#starts the game
start_screen_hangman()