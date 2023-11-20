# This program implememts a Hash Table with the Separate Chaining technique to deal with collision
class Node:
    def __init__ (self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__ (self, capacity):
        self.capacity = capacity        # capacity is the number of slots available
        self.size = 0                   # the number of key-value pairs that are already stored in the HashTable
        self.table = [None] * capacity  # [None] is Python's way to write an empty slot. '[None] * capacity' is an array of available slots
                                        # e.g. If capacity = 5, self.table = [None, None, None, None, None] Each "None" slot is available to store new value
    def _hash(self, key):
        return hash(key) % self.capacity

    def search(self, key):
        i = self._hash(key)
        current = self.table[i]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)

    def insert(self, key, value):
        i = self._hash(key)         # Calculate the index where the pair should be stored using the ‘_hash‘ method

        if self.table[i] is None:            # If there is nothing at that index,
            self.table[i] = Node(key, value) # it creates a new node with the key-value pair and sets it as the head of the list.
            self.size += 1
        else:                               # If there is a linked list at that index,
            current = self.table[i]
            while current is not None:      # iterate through the linked list.
                if current.key == key:      # If it finds the key,
                    current.value = value   # it updates the value.
                    return
                current = current.next
            new_node = Node(key, value)       # If it doesn’t find the key, it creates a new node,
            new_node.next = self.table[i] # and adds it to the head of the list.
            self.table[i] = new_node
            self.size += 1

    def remove(self, key):                  # remove() method removes a key-value pair from the hash table
        i = self._hash(key)                 # Gets the index where the pair should be stored using the '_hash' method

        if self.table[i] is None:
            print(key, "doesn't exist in hash table")
            return
        elif self.table[i].key == key:        # if we find the key at the head of the linked list at the index,
            self.table[i] = None            # we set this node as None (i.e. delete)
            self.size -= 1
            return
        else:                               # if we find the key at a position that's not the head,
            current = self.table[i].next    # we create a local variable "current" to keep track of the node we're looking at, and set its initial state as the next node of the head
            previous = self.table[i]        # create another local variable "previous" to keep track of the node before the node we're looking at, and set its initial state as the head
            while current is not None:      # traverse through the linked list
                if current.key == key:      # if we find the key in the linked list
                    previous.next = current.next    # point the previous node to the node after the current node (i.e. skip the current node). Now the current node is just floating in the space and there's essentially no way to keep track of it, so it can be considered deleted.
                    self.size -= 1
                    return
                previous = previous.next    # can i exchange these two lines?
                current = current.next
        print(key, "doesn't exist in hash table")




# Test code
hashtable = HashTable(5)                         # Create a hashtable object with the capacity of 5
#hashtable.insert("Goomba", "shmol")   # insert a key-value pair: Goomba-shmol
#print(hashtable.search("Goomba"))               # print out the search result of the key-value pair we just stored
hashtable.remove("goomba")



