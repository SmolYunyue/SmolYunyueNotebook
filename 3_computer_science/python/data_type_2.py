# special method __bool__() for statements
print(type((5==3).__bool__()),(5==3).__bool__(),
      id((5==3).__bool__()),id(False))

# special method __bool__() for numbers
print(type((0+3.5j).__bool__()),(0+3.5j).__bool__(),
      id((0+3.5j).__bool__()),id(True))

# sepcial method __len__() for strings
print(type("abcd".__len__()),"abcd".__len__(),
      id("abcd".__len__()),id(4))

# regular method is_integer() for floats
print(type((1.3).is_integer()),(1.3).is_integer())

# regular method as_integer_ratio() for floats
print(type((0.5).as_integer_ratio()),
      (0.5).as_integer_ratio())

# decimal in binary
x=0.1
print(x,f"{x:.17f}")

# standard library decimal
import decimal
print(type(decimal.Decimal("0.1")),"\n",
      f"{decimal.Decimal("0.1"):.50f}\n",
      f"{decimal.Decimal(0.1):.50f}")

# standard library fractions
import fractions
print(type(fractions.Fraction(1,10)),"\n",
      fractions.Fraction(1,10),fractions.Fraction("0.1"),
      fractions.Fraction(1,10)==decimal.Decimal("0.1"))

# regular method strip() for string
n="     abc  123     "
print(n,"\n",n.strip())

# regular method lower(), upper(), and casefold() for string
n="AbCdEf"
print(n.lower(),n.upper(),n.casefold())

# regular method replace() for string
n="banana"
print(n.replace("a","A",2),n.replace("a","A"))

# regular method split(), join() for string
n="123.456.789"
print(type(n.split(".")),n.split("."),
      type(",".join(n.split("."))),",".join(n.split(".")))

# string is immutable
n="123"
m=n.strip("3")
print(n is m,n,m)

# f-string examples
x=3.14159265358
print(f"Pi is approximately {x}\n",
      f"Pi is approximately {x:.4f}")

# precision
x=3.14159265358
print(f"{x:f}\n",
      f"{x:10f}")

# integer
print(f"{int(x):5d}\n",
      f"{int(x):<5d}\n",
      f"{int(x):^5d}\n",
      f"{int(x):>5d}\n",
      f"{int(x):0<5d}\n",
      f"{int(x):e^5d}\n",
      f"{int(x):x>5d}")