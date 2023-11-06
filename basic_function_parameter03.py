# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def sum(a):
    s=23652365236523
    for i in a:
        if i<s:
            s=i
    return s
print(sum([1, 2, 3, 4, 5]))