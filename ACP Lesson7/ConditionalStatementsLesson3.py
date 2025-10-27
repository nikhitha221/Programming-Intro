#AND
ans1 = input("What colour is the sky?")
ans2 = input("What is H20?")
if ans1.lower() == "blue" and ans2.lower() == "water":
    print("Correct")
else:
    print("Wrong")

#OR
ans1 = input("What colour is the sky?")
ans2 = input("What is H20?")
if ans1.lower() == "blue" or ans2.lower() == "water":
    print("One is correct")
else:
    print("Both are wrong")

#XOR
a = 5
b = 3
result = a ^ b
print("a =", a)
print("b =", b)
print("a ^ b =", result)

#NOT
is_raining = True
if not is_raining:
    print("You don't need an umbrella!")
else:
    print("Take an umbrella!")

#LEFTSHIFT
a = 19
b = 8
print("a >> 2 = " , a >> 2)

#RIGHTSHIFT
a = 68
b = 20
print("a << 2 = " , a << 2)