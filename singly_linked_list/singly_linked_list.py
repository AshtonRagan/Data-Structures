class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None  # this will be eaither None or a node
        self.tail = None

    def sayHI(self):
        return print("HELOW IM FROM SLL!!")

    def add_to_end(self, data):
        new_node = Node(data)  # this is making our node in the ether
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            print(f"inside the IF! data: {self.head.value}")
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node
            self.tail = new_node

    def add_to_front(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            cur = self.head
            self.head = new_node
            self.head.next = cur

    def remove_from_front(self):
        if self.head == None:
            return print("There nothing to remove")
        cur = self.head
        self.head = cur.next

    def remove_from_End(self):
        if self.head == None:
            return print("Nothing to remove")
        cur = self.head
        target = self.tail.value
        while target != cur.next.value:
            cur = cur.next
            # print(f"CV: {cur.value} T: {target} -> C: {cur.next.value}")
        self.tail = cur
        self.tail.next = None

    def length(self):
        cur = self.head
        total = 0
        while cur != None:
            total += 1
            cur = cur.next
        return print(f"Total in list: {total}")

    def printList(self):
        cur = self.head
        if cur == None:
            return print("No items in list")
        else:
            while cur != None:
                if cur.next == None:
                    print(f"{cur.value} -> None")
                    print(f"Head: {self.head.value}, Tail: {self.tail.value}")
                    return

                print(f"{cur.value} -> {cur.next.value}")
                cur = cur.next


a = linked_list()
a.add_to_end(1)
a.add_to_end(2)
a.add_to_end(3)
a.add_to_end(4)
a.add_to_front(5)
a.add_to_end(69)
a.length()
a.printList()
print("------------------")
a.remove_from_front()
a.remove_from_End()
a.length()
a.printList()
# a.printList()
