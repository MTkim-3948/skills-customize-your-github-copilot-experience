
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. You will create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Set up the game foundation by creating a word list and implementing the logic to randomly select a word for the player to guess.

#### Requirements
Completed program should:

- Maintain a predefined list of words to choose from
- Randomly select one word at the start of each game
- Initialize game variables (attempts remaining, guessed letters, word progress)
- Display the initial game state with underscores representing unguessed letters

### 🛠️ Letter Guessing and Progress Tracking

#### Description
Implement the core game loop that accepts player guesses and updates the game state accordingly.

#### Requirements
Completed program should:

- Accept letter guesses from the player
- Track correct and incorrect guesses separately
- Display current progress with guessed letters revealed (e.g., `_ _ _ _ _`)
- Show remaining attempts after each guess
- Prevent duplicate guesses and provide appropriate feedback

### 🛠️ Game Win/Loss Logic and End State

#### Description
Implement the logic to determine when the game ends and display appropriate win/lose messages.

#### Requirements
Completed program should:

- End the game when the player guesses the complete word (win condition)
- End the game when attempts reach zero (lose condition)
- Display a clear win message showing the word when player succeeds
- Display a clear lose message revealing the word when player fails
- Offer to play again or exit after game completion
