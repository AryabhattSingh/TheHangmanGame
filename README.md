# The Hangman Game

Welcome to The Hangman Game project! Put your word-guessing skills to the test and save the man from being hanged. This classic word-guessing game challenges you to uncover 
the hidden word using hints before your lives run out.

```bash
                                            +-----+
                                              |   |
                                              O   |
                                             /|\  |
                                             / \  |
                                                  |
                                            =========
```

## Overview

- **ASCII Art Start:** The game begins with captivating ASCII art that sets the mood for the hangman challenge.

- **Welcome Message:** Upon starting the game, the user is warmly welcomed to the hangman adventure.

- **Game Instructions:** Clear instructions on how to play the game are provided, ensuring that players understand the rules and objectives.

- **Hint for the Word:** A hint is given to help the player guess the mystery word. This adds an extra layer of fun and challenge.

- **Current Formed Word:** The current formed word, with correctly guessed letters filled in and unknown letters represented as blanks, is displayed to guide the
   player's guesses.

- **Hangman's Progress:** The current stage of the man, illustrating how many incorrect guesses have been made, is shown to intensify the game's thrill.

## Gameplay

1. The player is prompted to guess a letter in the word.

2. If the guessed letter exists in the mystery word:
   - The player is congratulated and informed that their lives count remains the same.
   - The remaining lives are displayed.
   - The current formed word is shown with correctly guessed letters filled in.
   - The current stage of the Hangman remains unchanged.

3. If the guessed letter does not exist in the mystery word:
   - Information is displayed to inform the player of their incorrect guess, and one life is deducted.
   - The remaining lives are displayed.
   - The current formed word remains the same (since the guessed letter is incorrect).
   - The current stage of the Hangman is updated to reflect the progress of the hangman drawing.

4. The process continues until the player either wins the game by correctly guessing the word before running out of lives or loses the game by using up all their lives
   and triggering the completion of the Hangman's figure.

5. The program is designed to handle various invalid inputs by the user, such as:
   - Not entering anything as a guess.
   - Entering a string instead of a single letter.
   - Inputting non-English alphabets or symbols.

## Getting Started

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/AryabhattSingh/TheHangmanGame.git
   ```

2. Navigate to the project directory:
   ```
   cd TheHangmanGame
   ```

3. Run the game:
   ```
   python main.py
   ```

4. Follow the on-screen instructions to play the game, guess letters, and save the man!

## Contributing

Contributions to this project are highly appreciated. If you have suggestions, enhancements, or bug fixes, feel free to submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

Have a great time guessing words and saving the Hangman! If you encounter any issues or have questions, please don't hesitate to reach out or open an issue.
Enjoy the challenge!"
