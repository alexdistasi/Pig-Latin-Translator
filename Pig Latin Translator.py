#Author: Alex DiStasi
#File: Pig Latin Translator.py
#Purpose: Program returns a sentence translated to pig latin



def pig_it(text):
    pig = "ay"
    #split incoming sentence into individual arrays based on spaces
    textArr = text.split()
    pigLatinSentence = ""
    #iterate through individual word
    for word in textArr:
        firstLet = word[0]
        for char in word:
            #check if a character in word is a punctuation mark
            if (char.isalpha()==False):
                pigLatinWord = word
            #take the word and remove the first character from beginning
            #move the first character to the end of the word and add "ay"
            else:
                pigLatinWord = word[1:]+firstLet+pig
        #form the full sentence in pig latin
        pigLatinSentence = pigLatinSentence +pigLatinWord + " "
    #return the sentence minus the space at the end
    return pigLatinSentence[:-1]
    

pigLatinIn= input("Enter a sentence. Write 'stop' to end: ")
while (pigLatinIn.lower() != "stop"):
    print (pig_it(pigLatinIn))
    pigLatinIn= input("Enter a sentence. Write 'stop' to end: ")
    
