# String and loop example

s = "PYTHON"

# for loop to print each character
for ch in s:
    print(ch)

# length of string
print(len(s))

# slicing
print(s[1:4])

# while loop with string index
i = 0
while i < len(s):
    print(s[i])
    i = i + 1


# List example
numbers = [10, 20, 30, 40]

numbers.append(50)
print(numbers)

numbers.remove(20)
print(numbers)

print(numbers[0])
print(len(numbers))

for n in numbers:
    print(n)


# Dictionary example
student = {
    "name": "Astra",
    "roll": 101,
    "marks": 85
}

print(student["name"])
print(student["roll"])

student["marks"] = 90
student["grade"] = "A"

for key in student:
    print(key, student[key])
