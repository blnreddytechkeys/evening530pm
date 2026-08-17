'''
itarative control stmt 
for 
while 
set of stmts execute more then one time based on cndiotio 
syntax:
for tempvariable in range([start],stop,[step]):
    code
    
    what is range()--> is a object it is used with for loop
    insted of doing for (init;condition;updation) 
'''
a=4
for i in range(0,11,2):
    print(f"{a} * {i} = {a*i}")
    
""" #given no i sperfect number or not 1 6
#input x=234
find pfno=?
pfno==x--> perfect no otherwise it is not perfect no
ex: x=6
pfno=1+2+3==>
if(pfno==x):
1+2+3=> 6
28==> 1,2,4,7,14 """