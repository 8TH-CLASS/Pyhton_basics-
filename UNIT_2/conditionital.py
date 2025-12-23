# Program to demonstrate if, if-else, if-elif-else, and nested if

num = 6


# 1. Simple if statement
# Checks only one condition
if num > 0:
    print("Number is positive")


# 2. if - else statement
# Checks even or odd
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# 3. if - elif - else (else-if ladder)
# Checks whether number is positive, negative, or zero
if num > 0:
    print("Positive number")
elif num < 0:          # elif = else if
    print("Negative number")
else:
    print("Zero")


# 4. Nested if statement
# Checks if number is positive and also checks even/odd
if num > 0:                    # outer if
    if num % 2 == 0:           # inner if
        print("Positive and Even")
    else:
        print("Positive but Odd")
else:
    print("Negative number")
