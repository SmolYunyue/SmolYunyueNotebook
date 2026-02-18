# print the identity, type, and the value for 4
print(id(4),type(4),4)
# type of any type is a type, the type itself is a type
print(type(type(4)))
print(type(type(type(4))))

# an example for binding
a,b=4,print
print(type(a),a,type(b),b,
      id(a),id(4),id(b),id(print))
b(a+5,"hello")

# an example for input function
n=input(f"{a} and hello\n")
print(type(n),n)

# an example for the above data types
print(type(True),True,type(1),1,
      type(1.0),1.0,type(1+0j),1+0j)

# subset example
if True==1==1.0==1+0j:
    print("Yes")
else:
    print("No")

# input string to number
n=input("type in an integer\n")
print(type(n),n,type(int(n)),int(n))

# identical map and canonical map
print(int(False),float(5),int(3.7))

# logic and bool
print(type(1==0))
print(type(""),bool(""))
if not "":
    print("statement or bool value defined can be used in logic")