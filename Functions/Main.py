def hello():
    print("Hello World !")

hello()

def add(x, y): # x, y are called Parameter
    return x+y

print(add(2,3)) # 2,3 are called Argument
print(add(4.5,7.9))

def list_print(arr):
    print(arr)

# Arbitrary Argument

def hello(* name):
    print(name)

hello("A","b","V")
