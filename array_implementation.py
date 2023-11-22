list = [1,1,2,3]

# Access and read:
print(list[0])

# Search: Method 1
if 1 in list:
    print(True)

# Search: Method 2
for n in list:
    if n == 1:
        print(True)
    break

# Insert: True Insert
list.insert(0, 55)
print(list)

# Insert: Append
list.append(55)
print(list)

# Insert: Extend
list.extend(["dog", "cat", "rat"])
print(list)

