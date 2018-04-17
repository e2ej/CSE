import random

'''
This is a guide of how to make hangman

1. Make a word bank
2. Select a random item to guess
3. Hide the word (use *)
4. Reveal letters based on input
5. Create win and lost conditions
'''

word_bank = ['tree', 'pencil', 'soccer', 'football', 'dog', 'basketball', 'computer', 'rock', 'intelligent', 'table',
             'hand', 'school', 'trash', 'backpack', 'gym', 'sweater', 'fresno', 'bird', 'food', 'pizza', 'little',
             'mexico', 'brazil', 'argentina']


word_choice = random.choice(word_bank)
strOne = word_choice
listOne = list(strOne)
"*".join(strOne)
print(listOne)
guesses = 10
while guesses >= 0:
    guess = input(">_")
    if guess == word_choice:
        print("You are correct.")
        break
    elif guess != word_choice:
        print('Your wrong!')
        guesses = guesses - 1
        print('You have %s guesses left' % guesses)
    if guesses == 0:
        print("You Suck ☺")
        break
