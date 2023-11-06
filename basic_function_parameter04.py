# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
def sum(a):
    s=0
    for i in a:
        s+=i
    return s//len(a)
print(sum([1, 2, 3, 4, 5]))