'''
for i in range([start],stop,[step]):
    #code
while(condition):
    #code

sum=0
for i in range(11):
    sum=sum+i
print("sum of natural numbers is ",sum)


sum=0
i=1# initilization 
while i<=20:#condition
    sum=sum+i
    i=i+1
print("sum of natural numbers is ",sum)
    

# sum of even numbers of n numbers
n=int(input("Enter limit number for even number sum "))
sum=0
i=1
while i<=n:
    if i % 2==0:# even number
        sum=sum+i
    i=i+1
print("sum of even  natural numbers is ",sum)
'''
# wa menu driven appilcation for basic maths
while True:
    print("=============== menu===============")
    print("for \n add enter +")
    print("subtraction enter -")
    print("multipication enter *")
    print("exit enter _")
    
    option=input("enter your option....")
    
    if option == "+":
        num1=int(input("enter a number "))
        num2=int(input("enter a number "))
        print(num1+num2)
    elif option == "-":
        num1=int(input("enter a number "))
        num2=int(input("enter a number "))
        print(num1-num2)
    elif option == "*":
        num1=int(input("enter a number "))
        num2=int(input("enter a number "))
        print(num1*num2) 
        
    elif option == "_":
        print("thank you")
        break  
    else:
        print("no valid option selected ...") 
