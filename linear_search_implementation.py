def linear_search (list, target): # this function finds the index of the target
    for i in range(len(list)):
        if list[i] == target: # list[i] retrieves an item with a given index i
            return i
    return None

# Test array
list = ["cat", "dog", "rat", "goblin", "soot"]
target = "soot"

# Function call
result = linear_search (list, target)

if result is not None:
    print("Target is found at index ", result)
else:
    print("Cannot find target")

