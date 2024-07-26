class cardHolderDetails():
    def __init__(self,CardNumber,Pin,FirstName,LastName,Balance):
        self.CardNumber=CardNumber
        self.Pin=Pin
        self.FirstName=FirstName
        self.LastName=LastName
        self.Balance=Balance
        
    ##print The details of cardHolder
    def get_cardNumber(self):
        return self.CardNumber
    def get_Pin(self):
        return self.Pin
    def get_FirstName(self):
        return self.FirstName
    def get_LastName(self):
        return self.LastName
    def get_Balance(self):
        return self.Balance
    
    #set The details of CardHolder

    def set_CardNumber(self,newValue):
        self.CardNumber=newValue
    def set_Pin(self,newValue):
        self.Pin=newValue
    def set_FirstName(self,newValue):
        self.FirstName=newValue
    def set_LastName(self,newValue):
        self.LastName=newValue
    def set_Balance(self,newValue):
        self.Balance=newValue
    
    #print All Details of cardHolder
    
    def display(self):
        print("cardNumber:",self.CardNumber)
        print("pin:",self.Pin)
        print("FirstName:",self.FirstName)
        print("LastName:",self.LastName)
        print("Balance:",self.Balance)
