from CardHolderDetails import cardHolderDetails

def print_menu():
    print("1.Deposit ")
    print("2.withdraw ")
    print("3.checkBalance ")
    print("4.Exit")

def Deposit(Newvalue):
    try:
        Deposit = float(input("How Much Money Do You Want To Deposit "))
        Newvalue.set_Balance(Newvalue.get_Balance()+Deposit)
        print("Thank You For Your Deposit And Your Balance is:",str(Newvalue.get_Balance()))
    except:
        print("Invaild Input...")
def withdraw(Newvalue):
    try:
        withdraw = int(input("How Much Money Do You Want To WithDraw:"))
        if (Newvalue.get_Balance()<withdraw):
            print("InSufficient Amount...")
        else:
            Newvalue.set_Balance(Newvalue.get_Balance()-withdraw)
            print("Pls Collect Your Amount...")
    except:
        print("InSufficient Amount...")

def checkBalance(Newvalue):
    print("Your Balance is:",Newvalue.get_Balance())

if __name__ == "__main__":

    object=cardHolderDetails("","","","","")

    DataBaseofCardHolderDetails=[]

    DataBaseofCardHolderDetails.append(cardHolderDetails("2345678909871234",8990,"Jagan","N.S",8000.00))
    DataBaseofCardHolderDetails.append(cardHolderDetails("2453768978905643",6514,"Hemanth","Kumar",17000.90))
    DataBaseofCardHolderDetails.append(cardHolderDetails("2135768901233452",1969,"Senthil","Kumar",19000.00))
    DataBaseofCardHolderDetails.append(cardHolderDetails("3145234567890987",1887,"Jothi","Lakshmi",6000.31))
    DataBaseofCardHolderDetails.append(cardHolderDetails("7878098976543213",7890,"Sathish","M.n",7000.89))
    DataBaseofCardHolderDetails.append(cardHolderDetails("9087654321343490",7890,"Mohit","yadav",5000.00))
    DataBaseofCardHolderDetails.append(cardHolderDetails("8767564315657901",1234,"vasanth","Kumar",6700.78))

    while True:
        try:
            DebitCardNumber = input("Enter DebitCardNo: ")
            DebitMatchInDB = [i for i in DataBaseofCardHolderDetails if i.CardNumber==DebitCardNumber]
            if len(DebitMatchInDB)>0:
                CurrentDatabase=DebitMatchInDB[0]
                break
            else:
                print("CardNumber is not recoginzed...")
        except:
            print("Insert The CardNumber...")
    while True:
        try:
            Pin = int(input("Enter The Pin: "))
            if (CurrentDatabase.get_Pin()==Pin):
                break
            else:
                print("This is Not Match For This is DebitCard...")
        except:
            print("This is Not Match For This is DebitCard...")

    print("Welcome",CurrentDatabase.get_FirstName(),CurrentDatabase.get_LastName(),":)")
    option=0
    while True:
        print_menu()
        try:
            option=int(input("Pls Select From One Of These Options:"))
        except:
            print("InVaild Option...")
        if option==1:
            Deposit(CurrentDatabase)
        elif option==2:
            withdraw(CurrentDatabase)
        elif option==3:
            checkBalance(CurrentDatabase)
        elif option==4:
            break
    print("Thank You For Visting Our ATM..")


