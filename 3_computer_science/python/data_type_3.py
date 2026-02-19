# list
a,b,c,d=[],[1],[1,],[1,2,3]
print(type(a),type(b),type(c),type(d),
      a,b,c,d)

# tuple
a,b,c,d=(),(1),(1,),(1,2,3)
print(type(a),type(b),type(c),type(d),
      a,b,c,d)

# regular method append() for list
a=[1,2]
b=a
c=a.append(3)
print(type(c),c,b,b is a)

# regular method extend() for list
a=[1,2]
b=[1,2]
print(a.extend([3,4]),b.append([3,4]),a,b)
a=[1,2]
a.extend("abc")
print(a)

# regular method insert(), pop(), index(), clear() for list
a=[1,3,4,5,5,6,7]
print(a.insert(1,2),a)
print(a.pop(),a,a.pop(0),a)
print(a.index(6))
try:
      print(a.index(7))
except ValueError:
      print("Value Error, cannot find the number 7 in a")
print(a.clear(),a)

# regular method count(), remove() for list
a=[1,2,3,4,5,5,5,5,5,5,5,6]
print(type(a.count(5)),a.count(5),a.remove(5),a,a.count(5))
for i in a:
      if a.count(i)>1:
            for _ in range(a.count(i)-1):
                  a.remove(i)
print(a)

# regular method copy(), reverse() for list
a=[1,2,3,4]
b=a.copy()
print(a is b,a.reverse(),a,b)

# copy()'s elements still shared
a=[[1,2],[3,4]]
b=a.copy()
a.reverse()
print(a,b)
b[0][0]=999
print(a,b)

# deep copy
import copy
a=[[1,2],[3,4]]
b=copy.deepcopy(a)
a.reverse()
print(a,b)
b[0][0]=999
print(a,b)