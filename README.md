# wordleCheater
A Python command-line tool to help solve the New York Times "Wordle" puzzle by narrowing down possible word choices based on your guesses.

## Features

- **Smart Word Filtering**:
  - Handles correct letters in right position (`*`)
  - Handles correct letters in wrong position (`^`)
  - Handles absent letters (`x`)
  
- **Efficient Word List Management**:
  - Pre-sorted word list by starting letter for fast lookups
  - Dynamic filtering after each guess

- **Interactive Interface**:
  - Shows remaining possible words count
  - Displays all possible words when under 20 remain
  - Input validation for guesses and corrections

## Technologies Used

- **Core**:
  - Python 3
  - Official Wordle word list from [tabatkins/wordle-list](https://github.com/tabatkins/wordle-list)

## Installation

1. Ensure you have Python 3 installed
2. Download the word list:
   ```bash
   wget https://github.com/tabatkins/wordle-list/blob/main/words