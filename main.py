import random
from words_list import words

class HangmanGame:
    def __init__(self):
        self.word = random.choice(words)
        self.guessed_letters = []
        self.mistakes = []
        self.tries = 6
        self.masked_word = ""

    def new_game(self):
        start = input("[N]ew game? or [E]xit?:  ")
        if start.lower() == 'n':
            self.reset()
            self.start_game()
        else:
            exit()

    def start_game(self):
        while self.tries > 0:
            self.guess(input("guess a letter: "))
            self.display_word()
            self.check_win()

    def guess(self, letter):
        if len(letter) > 1:
            print("only one letter")
            return
        elif letter in self.guessed_letters or letter in self.mistakes:
            print("you already checked this letter")
            return
        elif letter in self.word:
            self.guessed_letters.append(letter)
            print("hit!")
        else:
            self.tries-=1
            self.mistakes.append(letter)
            print(self.mistakes)
            print(f"{self.tries} tries")

    def display_word(self):
        self.masked_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                self.masked_word+=letter
            else:
                self.masked_word+="*"
        print(self.masked_word)

    def check_win(self):
        if self.masked_word == self.word:
            print("You won!")
            self.new_game()
            return
        else:
            self.check_loss()

    def check_loss(self):
        if self.tries == 0:
            print(f"The word was: {self.word}")
            self.new_game()
            return

    def reset(self):
        self.word = random.choice(words)
        self.guessed_letters = []
        self.mistakes = []
        self.tries = 6
        self.masked_word = ""


h = HangmanGame()
h.new_game()














