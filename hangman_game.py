
import random

words = ["python", "coding", "monkey", "school", "planet"]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\ |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\ |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\ |
      / \\ |
           |
    =========
    """
]



print("\n================================")
print("       WELCOME TO HANGMAN")
print("================================")

print("\nGuess the hidden word!")
print("You have 6 incorrect attempts.")


display_word = ["_"] * len(secret_word)


while wrong_guesses < max_attempts and "_" in display_word:



    print(hangman_stages[wrong_guesses])

    print("\nWord:", " ".join(display_word))
    print("Guessed letters:", guessed_letters)
    print("Wrong attempts:", wrong_guesses, "/", max_attempts)

  
    guess = input("\nGuess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:

        print("Correct guess!")

        for index, letter in enumerate(secret_word):
            if letter == guess:
                display_word[index] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

print("\n================================")

if "_" not in display_word:
    print("CONGRATULATIONS! YOU WON!")
    print("The word was:", secret_word)

else:
    print("GAME OVER!")
    print("The correct word was:", secret_word)

print("================================")
print("Thank you for playing Hangman!")
