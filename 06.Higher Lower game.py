import os

def HigherLowergame(dict,keys,score):
    logo ="""
               _                            _______     
              | |                          |__   __|    
 __      _____| | ___ ___  _ __ ___   ___     | | ___   
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \  
  \ V  V /  __/ | (_| (_) | | | | | |  __/    | | (_) | 
   \_/\_/_\___|_|\___\___/|_| |_| |_|\___|    |_|\___/  
   | |  | (_)     | |                                   
   | |__| |_  __ _| |__   ___ _ __                      
   |  __  | |/ _` | '_ \ / _ \ '__|                     
   | |  | | | (_| | | | |  __/ |                        
   |_|  |_|_|\__, |_| |_|\___|_|                        
        | |   __/ |                                     
        | |  |___/___      _____ _ __                   
        | |    / _ \ \ /\ / / _ \ '__|                  
        | |___| (_) \ V  V /  __/ |                     
    ____|______\___/ \_/\_/ \___|_|                     
   / ____|                                              
  | |  __  __ _ _ __ ___   ___                          
  | | |_ |/ _` | '_ ` _ \ / _ \                         
  | |__| | (_| | | | | | |  __/                         
   \_____|\__,_|_| |_| |_|\___|                         
"""
    print(logo) 
    logo2="""
 __      _______ 
 \ \    / / ____|
  \ \  / / (___  
   \ \/ / \___ \ 
    \  /  ____) |
     \/  |_____/ 
"""    
    for i in range(len(keys)-1):
        print("Compare 1:",keys[i])
        print(logo2)
        print("compare 2:",keys[i+1])
        print()
        value_of_1=dict[keys[i]]
        value_of_2=dict[keys[i+1]]
        select=input("Who has More Followers Type:Higher or Lower:").title()
        if select=="Higher":
            if value_of_1>value_of_2:
                score=score+1
                os.system("cls")
                print("Your Score is:",score)
            else:
                os.system("cls")
                print(f"{keys[i+1]} Have Greater Followers Than {keys[i]}")
                print("Sorry Your Answer is Wrong So You Lose")
                print("Your Final Score is:",score)
                break
        elif select=="Lower":
            if value_of_2>value_of_1:
                score=score+1
                os.system("cls")
                print("Your Score is:",score)
            else:
                os.system("cls")
                print(f"{keys[i]} Have Greater Followers Than {keys[i+1]}")
                print("Sorry Your Answer is Wrong So You Lose")
                print("Your Final Score is:",score)
                break
    else:
        print("The Game Over")    
dict_of_1={"NASA, a space agency, From United States":97900000,"T-seires, a Music Label & Movie studio, From India":7900000,"Narendra Modi, a prime Minister, From india":88100000,"Anirudh Ravichander , a Musician ,From India":9600000}
keys_of_1=list(dict_of_1.keys())
score_of_1=0
# HigherLowergame(dict_of_1,keys_of_1,score_of_1)

dict_of_2={"Justin Bieber, a Musician , From Canada":292000000,"Neeraj Chopra, a Athlete, from India":8700000,"Jennifer Lopez, a Musician & actress, From United States":267000000,"Shakira, a Musician, From colombia":90500000}
keys_of_2=list(dict_of_2.keys())
score_of_2=0
HigherLowergame(dict_of_2,keys_of_2,score_of_2)




