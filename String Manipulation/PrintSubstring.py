s = input("Enter A String : ")
for i in range (0, len(s)):
    for j in range(0, i+1):
        print(s[j], end=" ")
    print()

# Odd & Even Position Character

for i in range(len(s)):
    if i % 2 == 0:
        print( s[i])
for i in range(len(s)):
    if i % 2 != 0:
        print( s[i])

p = ""
s = "af {}"
for i in s:
    if i not in p:
        p += i
print(p)
print(p.format(s))
