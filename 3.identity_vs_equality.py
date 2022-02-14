# condiitons
a = 1
b = 1.0
c = "1"

if (a == c):
    print("it's a match")
elif(a == b):
    print("a match b")
else:
    print("not a match")

# identity vs equality

print(a == b) #true equivalent to is differnt from idential to
print(a is b) #false
print(c == "1") #true

print(b == 1 and isinstance(b, int))

print(a)
print(float(a))
print(str(a) is c) #false