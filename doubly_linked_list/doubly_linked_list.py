"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node != None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        return f"Head: {self.head}, Tail: {self.tail}"

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # new_node = ListNode(value)
        # cur = self.head
        if self.head == None:
            # self.length += 1
            # self.head,self.tai = ListNode(value)
            self.__init__(node=ListNode(value))
        else:
            # print(f"INPUTED VALUE: {value}")
            self.head.insert_before(value)
            self.head = self.head.prev
            # print(self.head.value)
            self.length += 1
            # self.head = new_node
            # cur.prev = self.head
            # self.head.next = cur
            # print(f"{self.head.value} -> {self.head.next}")

            # print(f"INPUTTED VALUE: {value}")
            # print(f"{self.head.value}")

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        self.length -= 1
        cur = self.head
        self.head.delete()
        self.head = self.head.next
        # self.head.prev = None
        return print(cur.value)
        """
        cur = self.head
        self.head = cur.next
        self.head.prev = none
        return cur
        """

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        """
            self.tail = self.tail.add_after(value)
            self.tail = self.tail.next
        """
        if isinstance(value, ListNode):
            target = value.value
        else:
            target = value

        self.length += 1
        if self.tail == None:
            self.__init__(node=ListNode(target))
        else:
            self.tail.insert_after(target)
            self.tail = self.tail.next

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        """
        cur = self.tail
        self.tail.remove()
        self.tail = self.tail.prev
        """
        if self.tail == None:
            return
        self.length -= 1
        cur = self.tail
        self.tail.delete()
        self.tail = cur.prev
        # self.tail.next = None
        return cur.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        """
        loop to find node.val == ele.val
        remove this node.
        delted(ele)
        then add this node to front.
        add_to_front(node.val)
        """
        if isinstance(node, ListNode):
            target = node.value
        else:
            target = node

        cur = self.head
        while cur.next != None:
            if cur.value == target:
                # print(f"Target: {target}")
                # print(f"Current: {cur.value}")
                target = cur.value
                cur.delete()
                self.length -= 1
            cur = cur.next
        self.add_to_head(target)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if isinstance(node, ListNode):
            target = node.value
        else:
            target = node
        cur = self.head
        while cur != None:
            if cur.value == target:
                # print(f"Target: {target}")
                # print(f"Current: {cur.value}")
                target = cur.value
                cur.delete()
                self.length -= 1
            cur = cur.next
        self.add_to_tail(target)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if isinstance(node, ListNode):
            target = node.value
        else:
            target = node
        cur = self.head
        if cur.value == target:
            self.head.delete()
            self.head = cur.next

            # self.head.prev = None
            self.length -= 1
            # cur.delete()

        if self.tail.value == target:
            self.tail.delete()
            self.tail = self.tail.prev
            self.length -= 1

        while cur.next != None:
            if cur.value == target:
                cur.delete()
            cur = cur.next
        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        cur = self.head
        max = self.head
        if cur == None:
            return 0
        while cur != None:
            print(cur.value)
            if cur.value >= max.value:
                max = cur
            cur = cur.next
        return max.value

        """
        loop thur and check cur.value
        # while ele.next != none
        # if cur.value is < ele.vale
        # cur = ele
        end: return cur.value
        """
        pass

    def printList(self):
        cur = self.head
        i = 0
        if cur == None:
            return print("No items in list")
        else:
            print("Prev--Current--Next")
            while cur != None:
                i += 1
                msg = f" <- {cur.value} -> "

                if cur.next == None:
                    msg += "None"
                else:
                    msg += f"{cur.next.value}"

                if cur.prev == None:
                    msg = f"None" + msg
                else:
                    msg = f"{cur.prev.value}" + msg
                cur = cur.next
                print(f"{i}: {msg}")

            print(f"Head: {self.head.value}, Tail: {self.tail.value}")


a = DoublyLinkedList()
print(a)
a.add_to_tail(9)
# a.add_to_tail(8)
# a.add_to_tail(7)
a.printList()
print("-----")
a.delete(a.tail)
a.printList()

# a.add_to_head(5)
# a.add_to_head(6)
# a.add_to_head(7)
# a.add_to_tail(13)
# a.add_to_tail(45)
# a.add_to_tail(66)
# a.add_to_tail(8)
# a.add_to_tail(12)
# print(f"Length: {len(a)}")
# a.printList()
# print("------------------")
# # a.remove_from_head()
# # a.remove_from_tail()
# a.move_to_front(66)
# a.move_to_end(13)
# # a.delete(12)
# print(f"Length: {a.__len__()}")
# a.printList()
# print(f"Max value: {a.get_max()}")
