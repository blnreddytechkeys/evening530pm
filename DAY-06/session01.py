'''
#
# Q:student have 5 subjects  
    # /--> float
    # //--> floor division 
    #**--> a ** b
    # cali--> total_marks ,avg(float)
    #input -->  english,java,c,cpp,python marks 1--100 --<> int
    #100 to 80 --> A
    #79 to  55 --> B
    #54 to  35--> C
    #34 to 0 > F
    
    #output--total marks ,avg,grade
    

'''
for i in range(3,6,1):
    eng=int(input("enter english marks"))
    java=int(input("enter java marks"))
    c=int(input("enter C language marks"))
    cpp=int(input("enter C++ language marks"))
    python=int(input("enter python language marks"))
    total_marks=eng+java+c+cpp+python
    avg=total_marks/5

    if avg <= 100 and avg >= 80:
        grade="A"
    elif avg <= 79 and avg >= 55:
        grade ="B"
    elif avg <= 54 and avg >= 35:
        grade = "C"
    else:
        grade ="F"

    print(f"You achived total marks {total_marks} average {avg} grade is {grade} ")

print("Thank you")