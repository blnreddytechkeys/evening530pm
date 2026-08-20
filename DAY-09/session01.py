#reverse of the number input--> x=234  | output-->  rx=432
# 2. print number in words x=234       | output--> two three four 
x=int(input("enter a number"))
rx=0
rem=0
while x>0:
    rem=x%10
    rx=(rx*10)+rem
    x=x//10
print("reverse number is ",rx)
while rx>0:
    rem=rx%10
    rx=rx//10
    if rem==1:
        print("one")
    elif rem==2:
        print("two")
        

