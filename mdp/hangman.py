import random

# 1. Word Selection
word_list = ["python", "hangman", "programming", "computer"]
chosen_word = random.choice(word_list)
word_display = ["_" for _ in chosen_word]
guessed_letters = []
attempts = 6 # Example: 6 incorrect guesses allowed

# 3. Game Loop
while attempts > 0 and "_" in word_display:
    print("\n" + " ".join(word_display))
    print(f"Attempts left: {attempts}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

    guess = input("Guess a letter: ").lower()

    # Input Validation
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    # 4. Guess Processing
    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Incorrect guess!")
        # Add code here to display hangman stages

# 5. Game End Conditions
if "_" not in word_display:
    print("\n" + " ".join(word_display))
    print("Congratulations! You guessed the word!")
else:
    print("\nGame Over! You ran out of attempts.")
    print(f"The word was: {chosen_word}")