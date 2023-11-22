class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# A function that finds the sum of a tree with a given root
def sum(root):
    if root is None:
        return 0
    return root.data + sum(root.left) + sum(root.right)

# fill in data for my tree
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node2.left = node3
node2.right = node4
node3.left = node5
node3.right = node6

print(sum(None))



