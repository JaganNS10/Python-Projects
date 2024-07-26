import random
print("Welcome to Hangman Game :)")
print("You Have 6 Lives That is You Have 6 Attempts....")
print("The Word Based On Fruits Only Don't Think Other words...")
word_db=["apple","beautiful","potato","orange","pineapple"]
choosen_word = random.choice(word_db)
display=["_" for i in choosen_word]
stages=['''
       +-----+
       |     |
       o     |
      /|\    |
      / \    |
             |
             |
       =======
        ''','''
       +-----+
       |     |
       o     |
      /|\    |
      /      |
             |
             |
       =======''','''
       +-----+
       |     |
       o     |
      /|\    |
             |
             |
             |
       =======''','''
       +-----+
       |     |
       o     |
      /|     |
             |
             |
             |
       =======''','''
       +-----+
       |     |
       o     |
       |     |
             |
             |
             |
       =======''','''
       +-----+
       |     |
       o     |
             |
             |
             |
             |
       =======''','''
       +-----+
       |     |
             |
             |
             |
             |
             |
       =======''']

print(display)
lives=6
while True:
    Guessed_letter=input("Guess a Letter:").lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter==Guessed_letter:
            display[position]=Guessed_letter
    print(display)
    if Guessed_letter not in choosen_word:
        lives-=1
        print(f"Your Letter {Guessed_letter} is not present")
        print(f"You Have {lives} Lives...")
        if lives==0:
            print("You lose")
            break
    if len(display)==len(choosen_word):
        print("you win")
        break
    print(stages[lives])
