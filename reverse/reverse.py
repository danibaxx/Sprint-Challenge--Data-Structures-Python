class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # checking if node is none
        if node == None:
            return node
        if node.next_node == None:
            return node
        # save current 1st
        curr_node = node
        prev = None
        next_node = curr_node.next_node
        while curr_node:
            # starting at the current node, saving next node to next_node temp variable, storing value to moving from one node to the next 
            next_node = curr_node.next_node
            # reassigns curr_node.next_node pointer to be previous instead of the next_node
            curr_node.next_node = prev
            # taking curr_node and assigning it to be previous
            prev = curr_node
            # taking next_node and assigning it to curr_node 
            curr_node = next_node
        self.head = prev
        return prev





linked_list = LinkedList()
print(linked_list)
linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.add_to_head(3)
linked_list.add_to_head(4)
print(linked_list)
