class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return str(self.value)


class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def stringify(self): # 1 <-> 2 <-> 3
        s = ''
        current = self.head
        if current == None:
            print('Empty.')
            return
        while current:
            s += str(current.value) + ' <-> ' if current.next else str(current.value)
            current = current.next
        print(s)
        return s

    def add_head(self, value):
        new = Node(value)
        current_head = self.head

        if current_head == None:
            self.head = new
            self.tail = new
            return
        
        current_head.prev = new
        new.next = current_head
        self.head = new
        return

    def add_tail(self, value):
        if self.head == None:
            self.add_head(value)
            return
        new = Node(value)
        current_tail = self.tail
        current_tail.next = new
        new.prev = current_tail
        self.tail = new

    def remove_head(self):
        if self.head == None:
            print('List empty.')
            return
        current_head = self.head
        if current_head.next:
            current_head.next.prev = None
            self.head = current_head.next
            print('removed current head and set next node to head')
            return
        # only one value
        print('only one value. list now empty')
        self.head = None

    def remove_tail(self):
        if self.tail == None:
            print('empty')
            return
        
        if self.tail == self.head:
            self.remove_head()
            return

        current_tail = self.tail
        current_tail.prev.next = None
        self.tail = current_tail.prev
        print('current tail removed, new tail set')

    def remove_by_value(self, rem_value):
        if self.head == None:
            print('empty')
            return
 
        if self.head.value == rem_value:
            self.remove_head()
            return
        
        current = self.head.next
        while current:
            if current.value == rem_value:
                if current == self.tail:
                    self.remove_tail()
                    return
                current.prev.next = current.next
                current.next.prev = current.prev
                print('node removed')
                return
            current = current.next
        print('node with specified value not found')

    def remove_by_value_reverse(self, rem_value):
        # same as remove by value, but iterate backwards, starting at tail
        if self.head == None:
            print('empty')
            return

        if self.tail.value == rem_value:
            self.remove_tail()
            return
        
        current = self.tail.prev
        while current:
            if current.value == rem_value:
                if current == self.head:
                    self.remove_head()
                    return
                current.prev.next = current.next
                current.next.prev = current.prev
                print('value removed')
                return
            current = current.prev
        print('value with specified value not found')
        
    def remove_nth_value(self, n): # start at position 0
        if self.head == None:
            return

        if n == 0:
            self.remove_head()
            return

        position = 1
        current = self.head.next
        while current:
            if position == n:
                if current == self.tail:
                    self.remove_tail()
                    return
                current.prev.next = current.next
                current.next.prev = current.prev
                print(f'removed node with value: {current.value}')
                return
            position += 1
            current = current.next
        print('n too big')

    def get_middle(self): 
        fast = self.head
        slow = self.head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
        print(f'middle: {slow.value}')
        return slow
                


ll = DoublyLinkedList()

ll.add_head(2)
ll.add_head(5)
ll.add_head(1)

# ll.add_tail(15)
ll.add_tail(10)
ll.add_tail(15)

ll.stringify()

ll.remove_head()
# ll.remove_tail()

ll.remove_by_value_reverse(2)

# ll.remove_nth_value(5)

ll.get_middle()

ll.stringify()