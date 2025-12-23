# Conditional and loop blocks in Python



#JUST TO UNDERSTAND EVRYTHING IS GIVEN IN CONDITION AND LOOPING



# Conditional statements
num = 5
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

# for loop
for i in range(1, 6):
    print("For loop:", i)

# while loop
i = 1
while i <= 5:
    print("While loop:", i)
    i = i + 1

# Nested if inside for loop
for i in range(1, 6):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

# Nested loops example
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j, end=" ")
    print()
