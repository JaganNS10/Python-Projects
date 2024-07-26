import random

def game(i):
    while i>0:
        userInput_easy=int(input("Make a Guess:\n"))
        if userInput_easy!=stored_number:
            print("Your Guess is wrong")
            i=i-1
            print(f"You have only {i} attempts to Guess The Number...")
            print()
            if userInput_easy<stored_number:
                print("Your Guess is Too Low")
            elif userinput>stored_number:
                print("Your Guess is too High")
            
        elif userInput_easy==stored_number:
            print(f"Your Guess {userInput_easy} is Correct.The Guess Number is {stored_number}.You Win")
            break
    else:
        print("You Lose")
logo="""
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|
"""

print(logo)
variable=random.randrange(1,51)
stored_number=variable
print(stored_number)
print("You Have To Think Between 1 To 50 Numbers :)")
userinput=input("Choose Level of Difficulty....select Easy Or Hard:\n").lower()


if userinput=="easy":
    print("You Have 10 Attempts To Guess The Number:\n")
    Easy_Attempts=10
    game(Easy_Attempts)
elif userinput=="hard":
    print("You Have 5 Attempts To Guess The Number:\n")
    Hard_Attempts=5
    game(Hard_Attempts)
    