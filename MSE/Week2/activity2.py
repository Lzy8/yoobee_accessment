import random
import string


class WordGuessGame:
    # List of possible secret words for the game.
    WORDS = [
        "python", "variable", "function", "iterator", "notebook",
        "pipeline", "dataset", "computer", "research", "analytics"
    ]

    def __init__(self, max_lives=6, secret_word=None):
        # Initialize the game state, including the secret word and blank placeholders.
        self.secret_word = secret_word or self.get_random_word()
        self.blanks = self.make_blanks(self.secret_word)
        self.max_lives = max_lives
        self.lives = max_lives
        self.used_letters = set()

    @classmethod
    def get_random_word(cls):
        # Choose one word randomly from the WORDS list.
        return random.choice(cls.WORDS)

    @staticmethod
    def make_blanks(word):
        # Create a list of underscores matching the secret word's length.
        return ["_" for _ in word]

    def prompt_for_letter(self):
        # Ask the player to enter a new letter until a valid one is supplied.
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print(" → Please enter a single A-Z letter.")
                continue
            if guess in self.used_letters:
                print(" → You already tried that letter.")
                continue
            return guess

    def reveal_letters(self, letter):
        # Reveal all occurrences of the guessed letter in the secret word.
        found_any = False
        for i, ch in enumerate(self.secret_word):
            if ch == letter and self.blanks[i] == "_":
                self.blanks[i] = letter
                found_any = True
        return found_any

    def is_won(self):
        # Check whether the player has revealed every letter.
        return "_" not in self.blanks

    def is_lost(self):
        # Check whether the player has run out of lives.
        return self.lives <= 0

    def display_status(self):
        # Print the current progress of the guessed word.
        print(" ".join(self.blanks))

    def play(self):
        # Main game loop.
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret_word)} letters.")
        self.display_status()

        while True:
            guess = self.prompt_for_letter()
            self.used_letters.add(guess)

            if self.reveal_letters(guess):
                print("\n Well done, Nice job! You found a letter.")
                self.display_status()
                if self.is_won():
                    print("\n Congratulation! You guessed the word!")
                    print(f"Word: {self.secret_word}")
                    print("GAME OVER")
                    break
            else:
                self.lives -= 1
                print(f"\nNope. You lose a life. Lives left: {self.lives}")
                self.display_status()
                if self.is_lost():
                    print("\n Out of lives & Sad story!")
                    print(f"The word was: {self.secret_word}")
                    print("GAME OVER")
                    break


def play_game(max_lives=6):
    # Create a game instance and start play.
    game = WordGuessGame(max_lives=max_lives)
    game.play()


if __name__ == "__main__":
    play_game()
