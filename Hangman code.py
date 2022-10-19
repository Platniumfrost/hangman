import random


HANGMAN=(

    
"""
-------
|   |
|   O
| /-+-\\
|   +
|  |+|
|  | |
|
|
|
|
|
|
|
----------

""",
"""

|   |
|   O
| /-+-\\
|   +
|  |+|
|  | |
|
|
|
|
|
|
|
----------
""",

    )

MAX_WRONG=len(HANGMAN)-1
print(HANGMAN[len(HANGMAN)-1])


WORDS=("OVERUSE","CLAM","GUAM","TAFFETA", "FRIEND", "FAMILY", "SCHOOL", "FOOD", "SLEEP", "GAME")
##word_index=random.randint(o,len(WORDS))
##word=WORDS[word_index]
##print(word_index)


word=random.choice(WORDS)#the word to be guessed
so_far="o"*len(word)#one dash for each letter in word
used=[]#letters already guessed
wrong=0#number of wrong guesses player has made

print("Welcome to Hangman.Good luck!")
print(HANGMAN[0])
print()
print(so_far)
