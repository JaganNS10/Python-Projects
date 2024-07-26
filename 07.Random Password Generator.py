import random
class Password:
    password=[]
    def get_letters(self,letters):
      try:
          userInput_letters=int(input("How Many Letters Do You Want:\n"))
          for i in range(userInput_letters):
            resofletters=random.choice(letters)
            self.password+=resofletters
      except:
         print("Invaild Input...")
    def get_numbers(self,numbers):
      try:
          userInput_numbers=int(input("How Many Numbers Do You want:\n"))
          for j in range(userInput_numbers):
            resofnumbers = random.choice(numbers)
            self.password+=str(resofnumbers)
      except:
         print("Invaild Input...")
    def get_symbols(self,symbols):
      try:
         userInput_symbols=int(input("How Many Symbols Do You want:\n"))
         for k in range(userInput_symbols):
            resofsymbols = random.choice(symbols)
            self.password+=resofsymbols
      except:
         print("Invaild Input...")
    def display(self):
      random.shuffle(self.password)
      final_password = "".join(self.password)
      print(final_password)
print("Welcome To Password Genarator :)")
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=["!","@","#","$","%","&","*","(",")","-",'+']
object=Password()
object.get_letters(letters)
object.get_numbers(numbers)
object.get_symbols(symbols)
object.display()