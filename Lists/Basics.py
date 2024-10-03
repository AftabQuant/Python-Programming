arr = [1, 2, 3, 4, 5, "apple", "banana"]
print(type(arr))
print(arr)
for i in range(len(arr)):
    print(arr[i])

print(arr[:: -1])
print(arr[1: 5])
print(arr[-1: -5: -1])