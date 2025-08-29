from colorama import Fore, Back, Style

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(Fore.GREEN + "Node inserted at the beginning" + Style.RESET_ALL)

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(Fore.GREEN + "Node inserted at the end" + Style.RESET_ALL)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(Fore.GREEN + "Node inserted at the end" + Style.RESET_ALL)

    def insert_at_position(self, data, position):
        if position <= 0:
            print(Fore.RED, "position should be >= 1", Style.RESET_ALL)
            return
        new_node = Node(data)
        if position == 1:
            self.insert_at_beginning(data)
            return
        temp = self.head
        count = 1
        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1
        if temp is None:
            print(Fore.RED, "position out of range", Style.RESET_ALL)
            return
        new_node.next = temp.next
        temp.next = new_node
        print(Fore.GREEN + "Node inserted at position " + str(position) + Style.RESET_ALL)

    def display(self):
        temp = self.head
        while temp:
            print(Fore.BLUE, temp.data, Style.RESET_ALL, end="->")
            temp = temp.next
        print(Fore.BLUE, "none", Style.RESET_ALL)


sll = SinglyLinkedList()
sll.insert_at_end(10)
sll.insert_at_beginning(5)
sll.insert_at_position(7, 2)
sll.display()