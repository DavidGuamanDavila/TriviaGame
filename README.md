# Trivia Game Project
## Project Overview
"Trivia Game" is an interactive Python-based trivia game designed for Arduino, combining elements of various subjects including Math, History, Chemistry, and Physics. Developed as part of the ENGI 1020 Lab-Mini Project, this game is tailored to provide an entertaining and educational experience for users, challenging their knowledge across different fields.

## Game Description
In "Trivia Game," players are quizzed with random questions from four major categories - Math, History, Chemistry, and Physics. The game utilizes a rotary dial for selecting question categories and an LCD screen for displaying questions and their respective categories. Players input their answers using a keyboard. Correct answers earn the player points, and the game continues until a set point threshold is reached or a question is answered incorrectly.

## Key Features
- **Category Selection**: Utilizes a rotary dial for choosing the category of trivia questions.
- **Dynamic Question Display**: Questions are displayed on an LCD screen, with each category represented by a unique color.
- **Point System**: Correct answers earn points; the game aims to accumulate a certain number of points.
- **User Interaction**: Players input their answers through a keyboard.
- **Game Flow Control**: The game has loops and functions for seamless gameplay and user interaction.

## Game Mechanics
1. **Start of the Game**: Instructions are displayed regarding the answer format.
2. **Question Selection**: Based on the rotary dial input, a question from the 2. corresponding category is selected randomly.
3. **Answer Input**: The player inputs their answer through the keyboard.
4. **Scoring**: Correct answers add to the player's score. Incorrect answers lead to game over.
5. **End of the Game**: Option to replay or end the game.

## Installation and Requirements
- **Python**: A Python interpreter is required to run the script.
- **Arduino and Grove Shield**: Required for the hardware components like the rotary dial and LCD screen.
- **Dependencies**: engi1020.arduino for Arduino integration, random and time Python modules.

## Trivia Game Flow Chart
<p align="center">
  <img width="409" alt="Screenshot 2024-02-01 at 10 37 42 PM" src="https://github.com/DavidGuamanDavila/trivia_code/assets/92492748/d8ef101f-027a-4c3f-ac15-e8af6b3e8c81">
</p>
### Sample Outputs
#### Sampel Output if RDvalue is >= 0 and <= 255
<p align="center">  
  <img width="558" alt="Screenshot 2024-02-01 at 10 40 16 PM" src="https://github.com/DavidGuamanDavila/trivia_code/assets/92492748/aa93aadd-5eaa-4291-8c86-322f01359368">
</p>
**Description**: The LCD screen's output is "Math question!" and the background color is orange, while in the console, it printed a random math question, ﻿"What is the antiderivative of 1?"

#### Sample Output if RDvalue is > 255 and <= 510
<p align="center">  
  <img width="581" alt="Screenshot 2024-02-01 at 10 40 40 PM" src="https://github.com/DavidGuamanDavila/trivia_code/assets/92492748/34b3ac08-4801-4317-af57-97dcf9223062">
</p>
**Description**: The LCD screen's output is "History question!" and the background colour is green, while in the console it printed a random history question, ﻿"What is the main religion of the world?"


#### Sample Output if RDvalue is > 510 and <= 765
<p align="center">  
  <img width="536" alt="Screenshot 2024-02-01 at 10 41 00 PM" src="https://github.com/DavidGuamanDavila/trivia_code/assets/92492748/15e6e4d7-6fc0-445e-9ddc-5a7127045bdb">
</p>
**Description**: The LCD screen's output is "Chemistry question!" and the background colour is pink, while in the console, it printed a random chemistry question, "What is the name of a positively charged ion?"


#### Sample Output if RDvalue is > 765 and <= 1023
<p align="center">  
  <img width="595" alt="Screenshot 2024-02-01 at 10 41 34 PM" src="https://github.com/DavidGuamanDavila/trivia_code/assets/92492748/9329e75d-5e00-426f-bcbe-b67e1434c6f0">
</p>
**Description**: The LCD screen's output is "Physics question!" and the background colour is light blue, while in the console it printed a random physics question, "Fill in the blank: Physics is the study of the __? One word"

  
## Testing and Validation
Extensive testing was conducted to ensure reliability and accuracy in the game's operation, including function tests for each category, input manipulation, and loop efficiency. Challenges encountered during development were addressed through iterative testing and debugging.


## Acknowledgements
Special thanks to the ENGI 1020 course facilitators and peers for their support and guidance throughout the project's development.

