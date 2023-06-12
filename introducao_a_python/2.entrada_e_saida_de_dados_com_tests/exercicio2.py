import random
import sys

WORDS = [
    "cat",
    "elephant",
    "dog",
    "monkey",
    "duck",
    "chameleon",
    "bear",
    "moose",
    "rooster",
]
MAX_ATTEMPTS = 3

# exercicio 3 modificando script


def create_words_file(words):
    with open('words.txt', 'w') as words_file:
        for word in words:
            words_file.write(word + '\n')


def read_words_file():
    with open('words.txt') as words_file:
        words = words_file.read().split()
    return words


def draw_secret_word():
    words = read_words_file()
    secret_word = random.choice(words)
    scrambled_word = "".join(random.sample(secret_word, len(secret_word)))
    return secret_word, scrambled_word


def game(secret_word, scrambled_word):
    contador = 0
    print(contador)
    while MAX_ATTEMPTS > contador:
        guesses = str(input('Guess the word: '))
        if secret_word == guesses:
            print(f"You win: {secret_word}")
            sys.exit()
        else:
            contador += 1
            print(
                f"You lose: {scrambled_word},\nremaining attempts {contador}")


if __name__ == "__main__":
    create_words_file(WORDS)
    secret_word, scrambled_word = draw_secret_word()
    print(f"Scrambled word is {scrambled_word}")
    game(secret_word, scrambled_word)
