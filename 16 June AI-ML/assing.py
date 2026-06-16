# Mutable vs Immutable Parameters

# Immutable Example
def modify(s):
    s += " World"
    print(s)

text = "Hello"
modify(text)

print(text)


# Muatable Example
def modify_(lst):
    lst.append(100)
    print(lst)

nums = [1, 2, 3]
modify_(nums)
print(nums)