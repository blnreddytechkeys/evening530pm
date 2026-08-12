'''
program: ifdemo.py
 description: 
 1.find even or odd number
 2. given no is positive or negative or zero
 about :
 conditional stmts  keywords: if ,else ,elif 
 keywords or reserved words for python 
 programmer can not use these keywords
    --as variable names
    --as function name 
    --as identifiers
if:
syntax:
--> when condition is True then execute the block of code
      
if condition: 
   code block
2.if   else:
if condtion is True then execute the block of code under if
if condition is False then execute the block of code under else 
syntax:
if condition: 
   code block
else:
   code block

num1= int(input("Enter a number: "))
reminder = num1 % 2
print(f"reminder is {reminder}")
if  reminder == 0: # reminder is 0 then it is even number
    print("Even")
if reminder != 0: # reminder is not 0 then it is odd number
    print("Odd")
    '''
#===============================
num1= int(input("Enter a number: "))
reminder = num1 % 2
print(f"reminder is {reminder}")
if  reminder == 0: # reminder is 0 then it is even number
    print("Even")
else: # reminder is not 0 then it is odd number
    print("Odd")

#2.given no is positive or negative or zero
if(num1 > 0):
    print("Positive number")
elif(num1 < 0):
    print("Negative number")
else:
    print("Zero")