ar = (1, 2, 3, 4, 5, "Apple", "Banana", "Cherry")
print(ar)
print(type(ar))

print("Length Of Tuple Is: ", len(ar))
print("Index Of Element: ",ar.index(5))

for i in ar:
    print(i, end=" ")
print()

[print(i, end=" ") for i in ar]
print()

# Slicing The Tuples
print(ar[1: 5])
print(ar[5:])
print(ar[:: -1])
print(ar[1:: 2])
