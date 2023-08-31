from word_treasury import *
from ascii_art import *
import random


def print_current_game_status():
    print("\nCurrent Formed Word: ", end="")
    for elements in display:
        print(elements, end=" ")
    print(stages[lives])


print(game_name)
print(welcome_message)

# picking a random word from the words_list
random_chosen_word = random.choice(words_list)
hint_of_chosen_word = hints_list[words_list.index(random_chosen_word)]

# converting the word into lowercase
random_chosen_word = random_chosen_word.lower()

print(f"""
Hint for the word:
------------------
{hint_of_chosen_word}""")

display = []
for letters in random_chosen_word:
    display += "_"

lives = 6
should_game_continue = True
already_input_letters = []

print_current_game_status()

while should_game_continue:

    user_input = input("Guess a letter: ").lower()

    # different checks on the user input
    if not user_input.isalpha():
        print("\nKindly enter English alphabets only.\n")
    elif len(user_input) > 1:
        print("\nKindly enter only a single alphabet.\n")
    elif user_input in display:
        print("\nYou have already guessed this letter in the word. Try a different alphabet.\n")
    elif user_input in already_input_letters:
        print("\nYou have already tried guessing this letter. Kindly try another alphabet.\n")
    else:

        already_input_letters += user_input

        if user_input in random_chosen_word:
            print_count = 0
            for i in range(len(random_chosen_word)):
                if random_chosen_word[i] == user_input:
                    if print_count == 0:
                        print(f"\nThis letter is in the word. Great job!\nRemaining Lives: {lives}")
                        print_count += 1
                    display[i] = random_chosen_word[i]
        else:
            lives -= 1
            print(f"\nThis letter is not in the word.\nYou lost one life.\nRemaining Lives: {lives}")

        print_current_game_status()

    if "_" not in display:
        print(f"The word \"{random_chosen_word}\" was correctly guessed with {lives} live(s) remaining.\nYou won!!!")
        should_game_continue = False

    if lives == 0:
        should_game_continue = False
        print("No more lives remaining.\nYou lost!")
