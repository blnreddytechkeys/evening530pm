import dis


a=2
b=3
def add(a,b):
    c=a+b
    return c

print("additon of two numbers ",add(a,b))

dis.dis(add)

