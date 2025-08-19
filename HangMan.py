import random

word_list = ["apple", "pizza", "train", "snake", "robot"]

word_to_guess = random.choice(word_list)
guessed_letters = []
attempts_left = 6

display_word = ["_"] * len(word_to_guess)

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {attempts_left} incorrect guesses allowed.")
print(" ".join(display_word))

while attempts_left > 0 and "_" in display_word:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!")
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[index] = guess
    else:
        print("❌ Wrong guess!")
        attempts_left -= 1

    print(f"\nWord: {' '.join(display_word)}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts_left}")

if "_" not in display_word:
    print("\n🎉 Congratulations! You guessed the word!")
else:
    print(f"\n💀 Game Over! The word was '{word_to_guess}'.")
