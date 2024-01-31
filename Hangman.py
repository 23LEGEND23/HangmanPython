#import word bank(done)
import pandas as pd
import numpy as np
import random

eng_words=pd.read_table('Python/Projects/Hangman/wordlist.txt', sep = "\s+", header = None)
print()

#ask user if want easy, medium or hard difficult(done)
#easy is 1-5 letters, medium 5-10 letters, hard 10<
def difficulty():
    while True:
        diff=input("Pick your difficulty: easy(E), medium(M) or hard(H): ").upper()

        if diff=='E':
            print("Difficulty set to easy")
            size=[1,6]
            break;
        elif diff=='M':
            print("Difficulty set to medium")
            size=[5,10]
            break;
        elif diff=='H':
            print("Difficulty set to hard")
            size=[10,50]
            break;
        else:
            print("Please type only 'E','M'or'H'.")
    return size

#pick a random word with corresponding length(done)
#if word length is inbetween size then pick word and set size as word length
#make word into list format
def word_generate(size):
    while True:
        word=eng_words.iloc[random.randint(0,eng_words.shape[0])] #randomly pick word from dataframe
        word=list(word[0]) #make word into list

        if len(word)>=size[0] and len(word)<=size[1]: #check to see if length of word fits difficulty
            break
    return word

#display hangman and blank words with underscore(if got blankspace, show blank space)(havent hangman)
def make_answer(word):
    answer=word.copy()
    for x in range(len(answer)):
        if not answer[x].isspace():
            answer[x]='_'
    return answer

def printout(answer,hangman):
    print()
    print(answer)
    print("You have %d more chance" %(6-hangman))
    print()

#ask user input for a letter(must be a letter):(done)
def user_input():
    while True:
        letter=input("Enter a letter: ").strip().lower()
        if not letter.isalpha():
            print("It must be a letter!")
        elif len(letter)!=1:
            print("Only one letter")
        else:
            break
    return letter

#if got, replace underscores with the letter and add used letters to a set(can display if want)
#if letter alr used, tell user they used it alr
#if dont have letter, add one to hangman and add used letters to a set
def check(word, answer, letter, used_letters,hangman):
    if letter in used_letters:
            print("Letter is already used. Try another letter.")
            print("Used letters:")
            print(used_letters)
    elif letter in word:
        used_letters+=[letter]
        for x in range(len(word)):
            if word[x]==letter:
                answer[x]=letter
    else:
        print("%s is not in the word" %(letter))
        used_letters+=[letter]
        hangman+=1
    return answer, letter, used_letters,hangman

#then repeat until word finished or hangman finish
def condition(word, answer, hangman,win):
    if hangman==6:
        win=-1
    elif word==answer:
        win=1
    return win

#display win or lose
def result(win,word):
    print()
    if win==-1:
        print("You lose!!!")
    if win==1:
        print("YOU WIN!!!")
    print("The word is ")
    print(word)

#ask if wanna play again
def play_again():
    print()
    while True:
        play=input("Do you want to play again(y/n): ").lower()
        if play=='y':
            return 0
        elif play=='n':
            return 1


#main
hangman=0
used_letters=[]
win=0
play=0
while True:
    print("Let's play hangman")
    size=difficulty() #set difficulty
    word=word_generate(size) #generate new word
    answer=make_answer(word) #make hidden word

    while True:
        printout(answer, hangman)
        letter=user_input()
        answer, letter, used_letters,hangman=check(word, answer, letter, used_letters,hangman)
        win=condition(word, answer, hangman,win)
        if win!=0:
            break
    result(win,word)
    play=play_again()
    if play:
        break
print("Thank you for playing. Baii!")

#create graphical version later