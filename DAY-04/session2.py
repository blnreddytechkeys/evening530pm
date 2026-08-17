#find user is major or minor
#irrespective of condition two times if condition will check 
age =int(input("enter your age "))
if age >=18:
    print("you are major ..")
    print("you can select MLA with help of Elections")
else: 
#if age < 18:
    print("you are Minor..")
    print("you have time to participate in election but not now")
print("End Of the program...")   


purchase_amount=float(input("enter purchase amount :"))
if purchase_amount<=10000 and purchase_amount>5000:
    print("you got 10% discount")
else:
    print("Thankyou.. visit again")