'''
assignment operator:
'=' this operator is assignment operator
==================================================
Left Hand Side    =             Right Hand Side
===================================================
vraiable   #valid               variable          -->num2 = num1
expression  #not valid          Expression       --> num3 = num1+num2+23-34
constant    #not valid          Constant         --> num1 = 123
==========================================================================
rules to use assignment operator :
  1.LHS MUST be vraiable 
  2.LHS never accept 
            expression a+12 = b #not valid
            constant   12=a #not valid 
            


  3.RHS may it have 
            variable -->num2=num1
            Expression --> num3=num1+num2+23-34
            Constant --> num1=123

'=='--> comparison operator --> relational operator !=
num1 == input("enter a number")  <--10
num1=10
==

num1=123
print(f"{num1} is saved in location{id(num1)}")
num1*=11 #num1=num1+11
print(f"{num1} is saved in location{id(num1)}")
num2=0
num3=123
num3=num1+num2+23-34
print(f"{num1} is saved in location{id(num1)}")
print(f"{num2} is saved in location{id(num2)}")
print(f"{num3} is saved in location{id(num3)}")
# in python all variables are reference type only
#multiple assignment

x=23
a,b,c=10,x,x+3
print("\n")
print(f"{a} is saved in location{id(a)}")
print(f"{b} is saved in location{id(b)}")
print(f"{c} is saved in location{id(c)}")


a =int(input("enter amount.."))#10000<--
#print numbers in words --> ex a=10000 "ONE ZERO ZERO ZERO ZERO"
% mod 
# reverse the given no  23456 <--
x=23456
r=x%10
x//=10
6
23456//10
2345
----
5
<--- 2345%10
234<-- 2345//10


# output--> 65432
'''





