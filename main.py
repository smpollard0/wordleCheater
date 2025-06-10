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

# This function takes the letter that is not found in the word and which
# position in the word it is and removes those words from the possible words
def removeWordContainingAt(possibleWords, letter, location):
    if location == 0:
        possibleWords.pop(location)

    newPossibleWords = []
    
    for wordList in possibleWords:
        subList = []
        for word in wordList:
            if word[location] != letter:
                subList.append(word)
        newPossibleWords.append(subList)
    return newPossibleWords

def removeWordsNotContaining(possibleWords, letter):
    newPossibleWords = []
    for wordList in possibleWords:
        subList = []
        for word in wordList:
            if letter in word:
                subList.append(word)
        newPossibleWords.append(subList)
    return newPossibleWords

def removeWordsNotContainingAt(possibleWords, letter, location):
    if location == 0:
        possibleWords = [possibleWords[ord(letter) - ord("a")]]
        return possibleWords
    
    newPossibleWords = []
    for wordList in possibleWords:
        subList = []
        for word in wordList:
            if word[location] == letter:
                subList.append(word)
        newPossibleWords.append(subList)
    return newPossibleWords

def removeWordsContaining(possibleWords, letter):
    newPossibleWords = []
    for wordList in possibleWords:
        subList = []
        for word in wordList:
            if letter not in word:
                subList.append(word)
        newPossibleWords.append(subList)
    return newPossibleWords

def parseCorrections(possibleWords, guess, corrections):
    for i in range(len(corrections)):
        letter = guess[i]
        match corrections[i]:
            case '*':
                possibleWords = removeWordsNotContaining(possibleWords, letter)
                possibleWords = removeWordsNotContainingAt(possibleWords ,letter, i)
            case '^':
                possibleWords = removeWordContainingAt(possibleWords, letter, i)
                possibleWords = removeWordsNotContaining(possibleWords, letter)
            case 'x':
                possibleWords = removeWordsContaining(possibleWords, letter)
    return possibleWords

def playGame(possibleWords):
    numPossibleWords = sum(len(sublist) for sublist in possibleWords)
    while numPossibleWords > 1:
        print(f"{numPossibleWords} possible word(s)")
        if numPossibleWords < 20:
            words = ""
            for wordList in possibleWords:
                for word in wordList:
                    words += f"{word}, "
            print(words)
        
        guess = input("Enter guess: ")
        while len(guess) < 5:
            print("Guess too short. Try again: ")
            guess = input("Enter guess: ")

        corrections = input("Enter corrections: ")
        while len(corrections) < 5:
            print("Corrections too short. Try again: ")
            corrections = input("Enter corrections: ")

        possibleWords = parseCorrections(possibleWords, guess, corrections)
        numPossibleWords = sum(len(sublist) for sublist in possibleWords)

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
    for i in range(97,123):
        subList = []
        while ord(words[index][0]) == i:
            subList.append(words[index])
            # This feels like bad practice...
            if index == len(words)-1:
                break
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