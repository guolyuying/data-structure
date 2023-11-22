# Create a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Change the console representation of every Node object into the data stored in the node (dog, cat etc).
# If we don't do this __repr__, when you print a Node object, it'll print out the address where the node is stored, instead of the data stored in the node.
    def __repr__(self):
        return self.data

# Create a LinkedList class, purposes: 1) make a container to store the "head", 2) to print out the whole LinkedList
class LinkedList:
    def __init__(self, head):  # create a "head" attribute for LinkedList class. Now the concept of "head" exists in our program.
        self.head = head

# Push Method (insert node at the beginning of a linked list)
    def push(self, new_data):
        new_node = Node(new_data) # Allocate new node & put in data
        new_node.next = self.head # Point new node to the original head
        self.head = new_node    # Make new node the head

# Append Method (insert node at the end of a linked list)
    def append(self, new_data):
        new_node = Node(new_data) # Allocate new node & put in data
        new_node.next = None
        if self.head is None:     # If linked list is empty, make new node the head
            self.head = new_node
            return
        last = self.head          # Else traverse to the end of linked list
        while last.next is not None:
            last = last.next
        last.next = new_node      # Make the next of the last node the new node

# Insert Method (insert node after a given node)
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must be in the linked list")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def remove_after(self, prev_node):
        obsolete_node = prev_node.next
        prev_node.next = prev_node.next.next
        del obsolete_node

    # Utility function to print out a linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    # Utility function to print out a linked list
    def __repr__(self):
        str = "<< "
        node = self.head  # the initial state of the node is the head
        while node is not None:  # as the while loop goes on, the state changes to node2, node3, node4, node5, until node becomes None (i.e. the linked list ends)
            str += node.data + " "
            node = node.next
        return str + ">>"

# The push method can also be written outside of the LinkedList class, it'll look like this:
# But this is not preferred, because we wanna categorize functions neatly instead of laying everything under the sun
def push( some_linked_list, some_new_data ):
    new_node = Node( some_new_data )
    new_node.next = some_linked_list.head
    some_linked_list.head = new_node

# Function that counts the length of the linkedlist based on head
def count_nodes(head):
    count = 1           #initial condition
    current = head      #initial condition
    while current.next is not None:
        current = current.next
        count += 1
    return count

# The next two blocks of code are the actual content of the linked list
# Create instances of Node class
node1 = Node("dog")
node2 = Node("cat")
node3 = Node("rat")
node4 = Node("goblin")
node5 = Node("soot")

# Link every node to the next one
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Declare that node1 is the head
myLinkedList = LinkedList(node1)

#result = count_nodes(nod e1)
#print(result)

#print(node1, node1.next)

#print(myLinkedList)

#print(myLinkedList.head)

#myLinkedList.push("goomba")
#push(myLinkedList, "koopa")

#myLinkedList.append("gooslime")

#myLinkedList.insert_after(node4, "kingSlime")
#print(myLinkedList)

myLinkedList.remove_after(node4)
myLinkedList.print_list()
