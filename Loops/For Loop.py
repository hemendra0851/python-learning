# Print 0 to 4
for i in range(5):
    print(i)

# Print 0 to 10 with 2 steps: 0,2,4,6,8
for i in range(0,10,2):
    print(i)

# Print from a list
numbers = [1,4,6,8,2,9]
for var in numbers:
    print(var)
else:
    print("Inside else")

# Use of break statement inside the loop
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

# Program to show the use of continue statement inside loops
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
