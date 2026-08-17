purchae_value=float(input("enter your total shopping value"))
discount_amount=0.0
bill=0.0
if(purchae_value >=10000.00):
    discount_amount=purchae_value*0.10
    bill=purchae_value - discount_amount
    print("Total bill amount",bill)
    print("visit again..")
    
elif (purchae_value >=5000.00):
    discount_amount=purchae_value*0.05
    bill=purchae_value - discount_amount
    print("Total bill amount",bill)
    print("visit again..")
else:
    bill=purchae_value 
    print("Total bill amount",bill)
    print("visit again..")
    
    
    
    
    

