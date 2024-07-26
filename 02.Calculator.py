# class calculator():
#     def Function_one(self,first_number,pick_operation,second_number,result):
#         if pick_operation=="+":
#             sum=first_number+second_number
#             result.append(sum)
#             print("Your Result is:",sum)
#         elif pick_operation=="-":
#             sum=first_number-second_number
#             result.append(sum)
#             print("Your Result is:",sum)
#         elif pick_operation=="*":
#             sum=first_number*second_number
#             result.append(sum)
#             print("Your Result is:",sum)
#         elif pick_operation=="/":
#             sum=first_number/second_number
#             result.append(sum)
#             print("Your Result is:",sum)
#     def Function_Two(self):
#         print(result)
#         operation=["+","-","*","/"]
#         for i in operation:
#                print(i)
#         pick_operation=input("Pick Anyone From These:\n")
#         second_number=int(input("Enter a Number:\n"))
#         if pick_operation=="+":
#             sum=result[-1]+second_number
#             result.append(sum)
#             print("Your Result is:",sum)
#         elif pick_operation=="-":
#             sum=result[-1]-second_number
#             result.append(sum)
#             print("Your Result is:",sum)
#         elif pick_operation=="*":
#             sum=result[-1]*second_number
#             result.append(sum)
#             print("Your Result is:",sum)
#         elif pick_operation=="/":
#             sum=result[-1]//second_number
#             result.append(sum)
#             print("Your Result is:",sum)


# result=[]
# first_number=int(input("Enter a Number:\n"))
# operation=["+","-","*","/"]
# for i in operation:
#     print(i)
# pick_operation=input("Pick Anyone From These:\n")
# second_number=int(input("Enter a Number:\n"))
# object=calculator()
# object.Function_one(first_number,pick_operation,second_number,result)

# while True:
#      userInput=input("Do You Want to Continue With Same Process Select 'x' or New Process Select 'y' or You want To Exit Select 'z':\n")
#      if userInput=="x":
#          object.Function_Two() 
#      elif userInput=="y":
#          result=[]
#          print(result)
#          first_number=int(input("Enter a Number:\n"))
#          operation=["+","-","*","/"]
#          for i in operation:
#              print(i)
#          pick_operation=input("Pick Anyone From These:\n")
#          second_number=int(input("Enter a Number:\n"))
#          object.Function_one(first_number,pick_operation,second_number,result)
#      else:
#          print("Thank you :)")
#          break
import os   
def add(a,b):
    return a+b          
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
operation={"+":add,"-":sub,"*":mul,"/":div}
def cal():
    pick_number1=int(input("enter Number1:"))
    for i in operation:
        print(i)

    while True:
        select=input("select operation:")
        pick_number2=int(input("enter Number2:"))
        get_operation=operation[select](pick_number1,pick_number2)
        result=f"The Result is {pick_number1}{select}{pick_number2}={get_operation}"
        print(get_operation)
        print(result)
        process=input("old one select x or new one select y or exit press z:")
        if process=="x":
            pick_number1=get_operation
            for i in operation:
                print(i)
        elif process=="y":
            os.system("cls")
            cal()
        elif process=="z":
            break
cal()
    