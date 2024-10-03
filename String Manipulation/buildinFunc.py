a = "Hello"
b = "Hello123"
c = "123456"
d = "HELLO"
e = " "
f = "1.234"
g = 1.234
# isalnum() : is alphanumeric
print(a.isalnum()) # True
print(e.isalnum())
print(f.isalnum())# False

# isalpha() : is alphabet
print(a.isalpha())
print(c.isalpha())

# isdecimal() : is decimal number
print(a.isdecimal())
print(f.isdecimal()) # False
print(c.isdecimal()) # True

# isdigit() : is digit in String
print(c.isdigit())

# isspace() : check if space is present or not
print(e.isspace())

