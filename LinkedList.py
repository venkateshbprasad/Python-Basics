class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Point current tail to new node
            self.tail = new_node       # Update tail reference
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            print("Index out of bounds.")
            return None
        if index == 0:
            removed_node = self.head
            self.head = self.head.next
            removed_node.next = None
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            removed_node = temp.next
            temp.next = removed_node.next
            removed_node.next = None
            if index == self.length - 1:
                self.tail = temp
        self.length -= 1
        return removed_node.value


my_linked_list = LinkedList(4)
my_linked_list.append(10)
my_linked_list.append(20)
my_linked_list.prepend(1)
my_linked_list.print_list()

print("Removed:", my_linked_list.remove(2))
my_linked_list.print_list()
