from wordlist import words
import random

def get_word(words):
    # Pre-condition: function takes in word
    # Post-condition: function keeps choosing new word until word is valid (does not have "-")
    correct_word = (random.choice(words))
    while '-' in correct_word:
        correct_word = (random.choice(words))
    return correct_word.upper()

def play_game():
    # Pre-condition: function takes no arguments
    # Post-condition: function dictates how game is actually played

    correct_word = get_word(words)
    unguessed_word = list('_' * len(correct_word))
    guessed = False
    guessed_letters = set()
    attempts = 0
    lives = 6

    print("Welcome to Hangman! You have {} lives.".format(lives))

    while guessed == False and lives > 0:
        guess = raw_input("Please guess a letter: ").upper()

        if len(guess) == 1 and guess.isalpha(): # Guess can only be a single alphabetic letter
            # If guessed letter is in word, convert word to list and replace "_" in unguessed word with guessed letter
            if guess in correct_word:
                list(correct_word)
                for i in range(len(correct_word)):
                    if correct_word[i] == guess:
                        unguessed_word[i] = correct_word[i]
                # When there are no more "_"s in the unguessed word --> game is won
                if "_" not in unguessed_word: 
                    guessed = True
                    print("Congratulations! You have guessed the word!")
                    print("The word was: " + ''.join(unguessed_word))
                    return
                # If there are still more "_"s in unguessed word, add letter to guessed letters, increment attempts,
                # convert unguessed_word word back to string, print results
                else:
                    guessed_letters.add(guess)
                    attempts += 1
                    print(" ").join(unguessed_word)
                    print("Attempt: {}\nLives left: {}").format(attempts, lives)
            
            # If guessed letter is not in word and is not a repeat guess, decrement lives
            elif guess not in correct_word:
                if guess not in guessed_letters:
                    lives -= 1
                # If all lives have been used, game is over
                if lives == 0:
                    print("Sorry! The correct word was {}".format(correct_word))
                    return
                # If there are still more "_"s in unguessed word, add letter to guessed letters, increment attempts,
                # convert unguessed_word word back to string, print results
                else:
                    guessed_letters.add(guess)
                    attempts += 1
                    print(" ").join(unguessed_word)
                    print("Attempt: {}\nLives left: {}").format(attempts, lives)

            letters_guessed = " "
            print("These are the letters you've guessed so far: " + letters_guessed.join(guessed_letters) + "\n")

        else:
            print("Not a valid guess")
    
    return

def main():
    get_word(words)
    play_game()

if __name__ == "__main__":
    main()
