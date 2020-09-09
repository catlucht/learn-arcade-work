# Ch.10 If Statements

a = 5
b = 4

if a < b:
    print("a is less than b.")

if a > b:
        print("a is greater than b.")

if a <= b:
    print("a is less than or equal to b.")

if a >= b:
    print("a is greater than or equal to b.")

# Just = is an assignment symbol so it can not be used in this context
# 1 is tell, 2 is ask
if a == b:
    print("a is equal to b.")

if a != b:
    print("a does not equal b.")

if a == 5 and b == 5:
    print("yay")

if a == 5 or b == 5:
    print("cool")

# Incorrect
if a > 5 and < 15:
    print("wrong")
    
# Correct
if a > 5 and a < 15:
    print("correct")

print("Done")

