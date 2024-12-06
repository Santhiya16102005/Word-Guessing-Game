import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "peach"]
    return random.choice(words)

def guess_word():
    word = choose_word()
    guessed_word = ["_"] * len(word)
    attempts = 0
    max_attempts = 6

    print("Welcome to the Word Guessing Game!")
    print(" ".join(guessed_word))

    while attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print(" ".join(guessed_word))
            if "_" not in guessed_word:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            attempts += 1
            print("Incorrect guess. Attempts left:", max_attempts - attempts)

    if "_" in guessed_word:
        print("Sorry, you've run out of attempts. The word was:", word)

guess_word()