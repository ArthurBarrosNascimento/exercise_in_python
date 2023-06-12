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


def draw_secret_word(words):
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
    secret_word, scrambled_word = draw_secret_word(WORDS)
    print(f"Scrambled word is {scrambled_word}")
    game(secret_word, scrambled_word)
