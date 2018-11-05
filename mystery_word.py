character_guesses = []
wrong_list = []
right_list = []

import random
random_choice = []

def easy_level():
    with open('words.txt') as stuff_file:
        for stuff in stuff_file.readlines():
            if len(stuff) > 4 and len(stuff) < 7:
                random_choice.append(stuff.strip())

def medium_level():
    with open('words.txt') as stuff_file:
        for stuff in stuff_file.readlines():
            if len(stuff) > 6 and len(stuff) < 8:
                random_choice.append(stuff.strip())

def hard_level():
    with open('words.txt') as stuff_file:
        for stuff in stuff_file.readlines():
            if len(stuff) > 8:
                random_choice.append(stuff.strip())

def lowercase_things(basket):
    input = basket.lower()
    return input

def choose_difficulty():
    difficulty = input("Welcome to Mystery Word! Would you like to play Mystery Word in Easy, Medium, or Hard Mode? ")
    difficulty = lowercase_things(difficulty)
    if difficulty == "easy":
        easy_level()
    elif difficulty == "medium":
        medium_level()
    elif difficulty == "hard":
        hard_level()
    else:
        print("That is not a valid choice! Please choose Easy, Medium, or Hard. ")
        choose_difficulty()

choose_difficulty()
random_word = random.choice(random_choice)
# print(random_word)


"""This Function shows an updated game board every time the user guesses"""
def print_game_board(test):
    new_list = []
    for x in test:
        if x in right_list and x.isalpha:
            new_list.append(x)
        else:
            new_list.append("_")
    return new_list
    
"""This function will lowercase any input"""
def lowercase_things(basket):
    input = basket.lower()
    return input

"""This function cleans the input and gives it too character_guesses IF it's valid"""
def clean_input(words):
    clean_word = words.lower()
    if clean_word in character_guesses:
        return "error"
    elif clean_word.isalpha() and len(clean_word) == 1:
        character_guesses.append(clean_word)
    return clean_word

"""This function will add the input to the right_list for EVERY TIME it appears in the word"""
def iteration(double_char):
    for x in random_word:
        if x == double_char:
            right_list.append(double_char)

"""This function plays the game, asking the user for their guess, then adds it to the appropriate lists"""
def game_board():
    while len(wrong_list) < 8:
        print(print_game_board(random_word))
        user_guess = input(f"You have {guesses_left(wrong_list)} guesses left. What is the letter you want to guess? ")

        clean_guess = clean_input(user_guess)

        if clean_guess == "error":
            print("You already guessed that letter. Try again!")
            continue
        elif clean_guess in random_word and clean_guess.isalpha():
            iteration(clean_guess)
        elif clean_guess not in random_word and clean_guess.isalpha() is True and len(clean_guess) == 1: 
            wrong_list.append(clean_guess)
        else:
            print("This is not a valid choice. Try again!")
            continue

        # print(f"Right List: {right_list}")
        print(f"Wrong List: {wrong_list}")

        if len(right_list) == len(random_word):
            print("You win!")
            break
        if len(wrong_list) == 8:
            print(f"You lose! The word was {random_word}")
            break
        
"""This function calculates how many guesses are left for the user"""
def guesses_left(bucket):
    list_left = 8 - len(bucket)
    return list_left



"""This function lets you choose whether to play again"""
def play_again():
    redo_choice = input("Do you want to play again? Type Yes or No ")
    redo_choice = redo_choice.lower()
    if redo_choice == "yes":
        choose_difficulty()
    elif redo_choice == "no":
        return
    else:
        print("Sorry, I didn't understand that!")
        play_again()

game_board()
play_again()