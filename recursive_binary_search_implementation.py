def recursive_binary_search(list, target):
    if len(list) == 0: # Stopping Condition 1: list is empty
        return False
    else:
        midpoint = (len(list))//2
        if list[midpoint] == target: # Stopping Condition 2: found the target at midpoint
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

# test list & test target
list = [1,2,3,4,5,6,7,8]
target = 2

# call function
result = recursive_binary_search(list, target)
print("Target found: ", result)

