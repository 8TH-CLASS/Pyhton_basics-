# continue example
for i in range(1, 6):
    if i == 3:
        continue       # skips current iteration
    print(i)

# break example
for i in range(1, 6):
    if i == 4:
        break          # terminates the loop
    print(i)

# else with loop
for i in range(1, 6):
    print(i)
else:
    print("Loop completed normally")   # executes only if loop not broken
