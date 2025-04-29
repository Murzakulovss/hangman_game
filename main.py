import random

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
mistakes=[]
tries = 6
display_word = ""

while tries > 0:
    player_guess = input("Guess a letter: ")
    if player_guess in word:
        guessed_letters.append(player_guess)
        print("hit!")
    else:
        tries-=1
        mistakes.append(player_guess)
        print("miss...")
        print(f"{tries} tries")

    for letter in word:
        if letter in guessed_letters:
            display_word+=letter
        else:
            display_word+= "*"
    print(display_word)

    if display_word == word:
        print("Победа!")
        break













