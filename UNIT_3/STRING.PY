s = input("Enter a string: ")
print("String:", s)

print("Length:", len(s))

print("First character:", s[0])
print("Last character:", s[-1])

print("Slice [0:5]:", s[0:5])
print("Every second character:", s[::2])
print("Reversed using slicing:", s[::-1])

s1 = "Hello"
s2 = "World"
print("Concatenation:", s1 + " " + s2)

print("Repetition:", s1 * 3)

print("Comparison s1 == s2:", s1 == s2)
print("Comparison s1 > s2:", s1 > s2)

print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

s_space = "  Python  "
print("After strip:", s_space.strip())

print("Replace 'a' with 'A':", s.replace("a", "A"))
print("Find 'g':", s.find("g"))

s_check = "Python123"
print("isalpha:", s_check.isalpha())
print("isdigit:", s_check.isdigit())
print("isalnum:", s_check.isalnum())

print("Characters in string:")
for ch in s:
    print(ch)

rev = ""
for ch in s:
    rev = ch + rev
print("Reversed using loop:", rev)
