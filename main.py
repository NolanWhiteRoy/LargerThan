# Compare two integers stroed strings without converting the strings to numbers.

# Input:
#  a: The first non-negative integer in string.
#  b: The second non-negative integer in string.
# Returns:
#  True if a is  than b.
#  False if a is smaller than or equal to b.


def larger(a, b):

    if len(a) > len(b):
        return True
    elif len(a)<len(b):
        return False

    for i in range(len(a)):
        if a[i]==b[i]:
            continue 
        elif a[i]>b[i]:
            return True
        else: # a[i]<b[i]
            return False
   
    return False # strings are the same value