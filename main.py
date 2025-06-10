#!/usr/bin/python3
'''
This program is meant to help me cheat at the NewYorkTimes game "Wordle".
Wordlist grabbed from https://github.com/tabatkins/wordle-list
'''

def printInstructions():
    instructions = "Corrections\n" \
    "* - correct letter, correct location\n" \
    "^ - correct letter, wrong location\n" \
    "x - letter not present\n"
    print(instructions)

def parseCorrections(possibleWords, corrections):

    for correction in corrections:
        match correction:
            case '*':
                pass
            case '^':
                pass
            case 'x':
                pass

    return

def playGame(possibleWords):
    while True:
        guess = input("Enter guess: ")
        while len(guess) < 5:
            print("Guess too short. Try again: ")
            guess = input("Enter guess: ")

        corrections = input("Enter corrections: ")
        while len(corrections) < 5:
            print("Corrections too short. Try again: ")
            corrections = input("Enter corrections: ")

        parseCorrections(possibleWords, corrections)

def loadWordList():
    words = []
    with open("./words", "r") as file:
        for line in file:
            words.append(str(line).strip())

    return words

# This function parses the word list into a list of lists where each index is a list
# of words that start with a certain letter
def parseWordList(words):
    index = 0
    parsedWordList = []
    for i in range(97,122):
        subList = []
        
        while ord(words[index][0]) == i:
            subList.append(words[index])
            index += 1

        parsedWordList.append(subList)

    return parsedWordList

def main():
    words = loadWordList()
    parsedWords = parseWordList(words)
    printInstructions()
    playGame(parsedWords)



if __name__ == "__main__":
    main()