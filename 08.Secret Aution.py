import os
print("************Welcome To The Secret Auction************")
dict={}
while True:
    userInput=input("What is Your Name?:\n")
    amount=int(input("What is Your Bid?:\n"))
    dict[userInput]=amount
    other_members=input("Is There Any other Bidders Type:'Yes' Or 'No':\n").lower()
    if other_members=="no":
        result=max(dict,key=dict.get)
        print(f"The Winner is {result} With {dict[result]} Amount :)")
        break
    else:
        os.system('cls' if os.name=='nt' else 'clear')