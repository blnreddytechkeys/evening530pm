'''
==========================================
date: 11/08/2026      topic: Operators
program:  session01.py
==========================================

arthamatic operators-->
all arthamatic operators are binary operators 
+ --> add   
  a+b--> a and b are operands/variables
         + operator
- -->substraction   
  a-b
* --> multipication 
a*b
/ --> division  
a/b
// --> floor division
a // b 
% --> modulas 
a % b
** ---> power 
a**b
'''
num1=int(input("enter a numaric value"))
num2=int(input("enter a numaric value.."))
result=num1+num2
print("Addition + : ",num1+num2)
print("subtraction -: ",num1-num2)
print("multipication * : ",num1 * num2)
print(" division Reminder % :",num1 % num2)  
print(" Division  / :",num1/num2) # float value --> value cofficient
print(" division result type is : ",type(num1 / num2))
print(" floor division co_efficient  //:",num1 // num2)
print(" floor division result type is : ",type(num1 // num2))
print(f" {num1} ** {num2} : {num1 ** num2}")


'''
# input() pre defined function()
# return value is string
# explicitly we have to convert to desired data type 
#str to int --> int(input())
# str to float --> float(input())

print("entered value is ",num1)
print("data type of the enterd value ..",type(num1))
print("entered value saved memory location id ",id(num1))
print("\n")
print("entered value is ",num2)
print("data type of the enterd value ..",type(num2))
print("entered value saved memory location id ",id(num2))
'''
