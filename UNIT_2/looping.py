# Program to demonstrate simple loops, range loops, while loop, and nested loops

# 1. Simple for loop using a list
numbers = [1, 2, 3, 4, 5]

for n in numbers:
    print(n)          # prints each element of the list


# 2. for loop using range() with one argument
# Prints numbers from 0 to 4
for i in range(5):
    print(i)


# 3. for loop using range(start, stop)
# Prints numbers from 1 to 5
for i in range(1, 6):
    print(i)


# 4. for loop using range(start, stop, step)
# Prints even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)


# 5. Reverse for loop using range()
# Prints numbers from 5 to 1
for i in range(5, 0, -1):
    print(i)


# 6. while loop
# Prints numbers from 1 to 5
j = 1
while j <= 5:
    print(j)
    j = j + 1      # update statement


# 7. NESTED FOR LOOP
# Outer loop runs 3 times
# Inner loop runs fully for each outer loop

for i in range(1, 4):            # outer loop
    for j in range(1, 4):        # inner loop
        print(j, end=" ")
    print()                      # new line after inner loop


# 8. NESTED WHILE LOOP

i = 1
while i <= 3:                    # outer while loop
    j = 1                        # reset inner loop variable
    while j <= 3:                # inner while loop
        print(j, end=" ")
        j = j + 1
    print()
    i = i + 1


# 9. for loop inside while loop

i = 1
while i <= 3:
    for j in range(1, 4):
        print(j, end=" ")
    print()
    i = i + 1
    
    
    
    # Loop manipulation using pass

# for loop with pass
for i in range(1, 6):
    if i == 3:
        pass        # does nothing, loop continues
    print(i)

# while loop with pass
i = 1
while i <= 5:
    if i == 2:
        pass        # placeholder statement
    print(i)
    i = i + 1

# empty loop body using pass
for i in range(5):
    pass            # loop executes with no action

