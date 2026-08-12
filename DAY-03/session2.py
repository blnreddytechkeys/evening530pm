'''
a=12
b=12
== --> comparison operator
binary operator
a == b
a =  b--> assignment operator
LHS=RHS  --> RHS is assigned to LHS

RHS u must be constant or variable or expression
v1=23
v2=v1
v3=v1+v2-12
24=v1--> invalid
v1+v2=v3 --> invalid
if a==b:
    print("a is equal to b")
control flow statement
--> it will control 
    the flow of execution of statements in a program
1.sequential
    ex: functions ,modules code etc
2.conditional
    if ,else ,elif 
    -->keywords or reserved words for python
3.looping 
    --> while, for
    
4.jumping 

    --> break, continue, pass ,exit(),return
'''
a=45
b=45
#a==b ==> result will True or False
#bool is a data type which can hold True or False

x=(a<b)
x=(a>b)
x=(a!=b)
x=(a==b)

print(f" {a} == {b}: {x}") # --> True 
print(type(x))# <class 'bool'>
print(id(x)) # --> memory address of x
 