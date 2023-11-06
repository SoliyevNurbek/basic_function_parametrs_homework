# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def vowels(s):
    k=0
    unli="aeiouAEIOU"
    for i in range(len(s)):
        if s[i] in unli:
            k+=1
    return k
print(vowels("eEcaOvioUI"))