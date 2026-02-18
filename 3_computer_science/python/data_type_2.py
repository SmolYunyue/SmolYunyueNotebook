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
import decimal as dec
print(type(dec.Decimal("0.1")),"\n",
      f"{dec.Decimal("0.1"):.50f}\n",
      f"{dec.Decimal(0.1):.50f}")