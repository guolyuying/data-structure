def binary_search (list, target):
    first = 0
    last = len(list)-1
    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

# Test array
list = [1.1, 4.3, 6.7, 8.9]
target = 6.7

# Function call
result = binary_search(list, target)
if result is not None:
    print("Target is found at index " + str(result))
else:
    print("Cannot find target")