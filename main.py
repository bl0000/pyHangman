import hangmanUI as hm
import wordslistCreator as wlC
import os
import random
import json
import re

def wordCollector():
    question = input("Do you want to use a custom wordslist? (y/n)\n")
    if question == "y":
        newQuestion = input("Would you like to create a custom wordslist now? (y/n)\n")
        if newQuestion == "y":
            jsonFileName = wlC.creator()
            wordslist = json.loads(open(jsonFileName).read())
            hangmanWord = wordslistRandomSelection(wordslist)
        else:
            print("Here are all the files in the directory:")
            files = os.listdir()
            for f in files:
                print(f)
            jsonFileName = input("Please enter the name of the file for your wordslist.\n")
            jsonFileName = jsonExtensionChecker(jsonFileName)
            wordslist = json.loads(open(jsonFileName).read())
            hangmanWord = wordslistRandomSelection(wordslist)
    if question == "n":
        cars = ["Lamborghini", "Ferrari", "Toyota", "Maserati", "Nissan", "Audi"]
        programmingLangs = ["Python", "HTML", "ObjectiveC", "Perl", "Ruby", "Swift", "LUA"]
        clothingBrands = ["Moncler","Balenciaga","Chanel","Dior","Billionaire Boys Club","Hugo Boss","Stone Island"]
        print("Please select one of the premade themes. Please note you can create your own wih the wordslist creator. \nPlease choose from cars, programming languages or clothing brands.")
        inp = input("(cars/langs/brands)\n")
        if inp == "cars":
            wordslist = cars
            hangmanWord = wordslistRandomSelection(wordslist)
        elif inp == "langs":
            wordslist = programmingLangs
            hangmanWord = wordslistRandomSelection(wordslist)
        elif inp == "brands":
            wordslist = clothingBrands
            hangmanWord = wordslistRandomSelection(wordslist)
    return hangmanWord.lower()

def underscoreConversion(word):
    nw = re.sub('[A-Za-z]', '_', word)
    return nw

def clear_screen():
    os.system('clear') # change clear to cls for Windows command prompt

def wordChecker(letter,word,nw, count, incorrectGuesses):
    letterCount = 0
    incorrectGuess = True
    for i in range(len(word)):
        if letter == word[i]:
            nw = nw[:(i)] + letter + nw[(i+1):]
            incorrectGuess = False
        else:
            letterCount += 1
            if letterCount == len(word):
                incorrectGuesses.append(letter)
    if incorrectGuess == True:
            count += 1
    return nw, count, incorrectGuesses

def jsonExtensionChecker(jsonFileName):
    if jsonFileName[-5:] != ".json":
        jsonFileName = jsonFileName + ".json"
    return jsonFileName

def wordslistRandomSelection(wordslist):
    randomWord = wordslist[random.randint(0,(len(wordslist))-1)]
    return randomWord

def ui(count, wordUnderscores, incorrectGuesses):
    clear_screen()
    print(hm.gui(count),"\nWord:\n", wordUnderscores, "\nIncorrect Guesses:\n", incorrectGuesses)

def main():
    count = 0
    incorrectGuesses = []
    word = wordCollector()
    wordUnderscores = underscoreConversion(word)
    clear_screen()
    while True:
        ui(count, wordUnderscores, incorrectGuesses)
        letter = input("Enter a letter: ")
        wordUnderscores, count, incorrectGuesses = wordChecker(letter,word,wordUnderscores, count, incorrectGuesses)
        if count == 7:
            ui(count, wordUnderscores, incorrectGuesses)
            print("YOU LOSE!\nThe word was:", word)
            break
        if wordUnderscores == word:
            ui(count, wordUnderscores, incorrectGuesses)
            print("YOU WIN!")
            break

if __name__ == "__main__":
    main()