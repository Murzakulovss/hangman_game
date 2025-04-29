import random
from operator import contains
from random import choice

def game():
    words = [
        "машина",
        "комната",
        "заводчик",
        "учитель",
        "письмо",
        "морозец",
        "проект",
        "трактор",
        "погода",
        "картинка",
        "сказание",
        "платформа",
        "праздник",
        "солнце",
        "столица",
        "пластик",
        "ключница",
        "галерея",
        "пещера",
        "ветерок"
    ]
    word = random.choice(words)
    guessed_letters = []
    mistakes = []
    tries = 6
    hangman_stages = [
        '''
           _______
          |/      
          |      
          |      
          |      
          |     
         _|___
        ''',
        '''
           _______
          |/      |
          |      (_)
          |      
          |      
          |     
         _|___
        ''',
        '''
           _______
          |/      |
          |      (_)
          |       |
          |       |
          |     
         _|___
        ''',
        '''
           _______
          |/      |
          |      (_)
          |      \|
          |       |
          |     
         _|___
        ''',
        '''
           _______
          |/      |
          |      (_)
          |      \|/
          |       |
          |     
         _|___
        ''',
        '''
           _______
          |/      |
          |      (_)
          |      \|/
          |       |
          |      / 
         _|___
        ''',
        '''
           _______
          |/      |
          |      (_)
          |      \|/
          |       |
          |      / |
         _|___
        '''
    ]
    while tries > 0:
        display_word = ""
        player_guess = input("Guess a letter: ")

        if len(player_guess) > 1:
            print("only one letter")
            continue
        elif player_guess in guessed_letters or player_guess in mistakes:
            print("you already checked this letter")
            continue
        elif player_guess in word:
            guessed_letters.append(player_guess)
            print("hit!")
        else:
            tries -= 1
            mistakes.append(player_guess)
            print(mistakes)
            print(f"{tries} tries")

        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "*"
        print(display_word)

        if display_word == word:
            print("Победа!")
            new_game()
            return
        if tries == 0:
            new_game()
            return

def new_game():
    start = input("[N]ew game? or [E]xit?:  ")
    if start.lower() == 'n':
        game()
    else:
        exit()

new_game()















