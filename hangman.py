import random

words = ["python", "computer", "programming", "developer", "coding"]

while True:
    secret_word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("\n==============================")
    print("       HANGMAN GAME")
    print("==============================")
    print("Guess the word one letter at a time.")

    while wrong_guesses < max_wrong_guesses:

        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter only.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess! 🎉")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in secret_word):
            print("\n🎉 Congratulations!")
            print("You guessed the word:", secret_word)
            break

    else:
        print("\n😢 Game Over!")
        print("The word was:", secret_word)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing Hangman! 👋")
        break