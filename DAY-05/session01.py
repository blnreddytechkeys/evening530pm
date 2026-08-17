'''
if 12<13:# ladder if
    pass
   #true block code
elif 12<14:# else if 
    pass
elif 12> 15:
    pass
else:
    pass
    #false block code
print("EOF")

logical operators:
 not--> unary operator
 not (12<13)  
 ====================
 truth table 
 ===================
  A     not A
 =================
 True   False
 False  True 
 ============================
 shoping
  pay amount ==> above or equal to 10000--> 10% on bill
             ==> 5000 to 9999  --> discount is 5% on bill
             ==> less than 5000 --> no discount give thanks msg
 and operator
  A= bill > 5000    B= bill < 9999
  ==================================
    A      B      A and B 
    =======================
    F      F        F
    T      F        F
    F      T        F
    T      T        T
=========================
    A       B      A or B
===========================
    F       F       F
    T       F       T
    F       T       T
    T       T       T    
 
 or--> binary operators

a=int(input("enter a number.."))
b=int(input("enter a number.."))
result=a==b
print("result is ",result)
#result=not(a<b)
result = not result

print("result is ",result)

& | ^ ! ~
     '''
print(" welcome to XYZshoppe..")
bill=float(input("enter your shopping bill amount"))
total_bill =0.0
dis=0.0
if(bill >= 10000):
    dis=bill*0.10
    total_bill=bill - dis
    print(f" your bill :{bill}\n ")
    print(f"discount :{dis}\n")
    print(f"finall bill {total_bill}")
    
if (bill > 5000) or (bill < 9999):
    dis=bill*0.05
    total_bill =bill -dis
    print(f" your bill :{bill}\n ")
    print(f"discount :{dis}\n")
    print(f"finall bill {total_bill}")
else:
    dis=0.0
    total_bill=bill-dis
    print(f" your bill :{bill}\n ")
    print(f"discount :{dis}\n")
    print(f"finall bill {total_bill}")
    