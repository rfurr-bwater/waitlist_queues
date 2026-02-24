class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class Queue:
    def __init__(self):
        self.head = None # Stores Node object
        self.size = 0
    
    def add(self,item): # Item is the data payload
        new_node = Node(item)
        if not self.head:
            self.head = new_node # New node becomes the head

        else: # Go to the head and add it
            current = self.head
            while current.next is not None: # Traverse the list to get to the end
                if current.next is None:
                    break
                current = current.next
            current.next = new_node
        self.size += 1 # Update the size

    def pop_left(self):
        '''Returns the left side'''
        if not self.head:
            return None
        current_head = self.head # Have to return
        self.head = self.head.next 
        self.size -= 1 # Update the size
        return current_head

    def is_empty(self):
        '''Check if the queue is empty'''
        if self.head: return False
        return True
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        return_str = "Queue Object: "
        for node in self: # Implicitly calls __iter__
            return_str = return_str + node.data + " -- "
        return return_str
    
    def __str__(self):
        return f"Queue Object: {self.head}"