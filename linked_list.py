from node import Node


class LinkedList:
    def __init__(self, values=None) -> None:
        self.head = None
        self.tail = None
        if values is not None:
            self.insert_end(values) if type(values) is not list else self.add_multiple(values)

    def __repr__(self):
        return f'Linked List that contains {self.length()} Nodes.'

    def length(self) -> int:
        count=0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def stringify(self):
        current = self.head
        string = ''
        while current:
            string += str(current.value) + ' -> ' if current.next else str(current.value)
            current = current.next
        return '\n' + string + '\n'

    def add_multiple(self, values):
        for value in values:
            self.insert_end(value)

    def insert_end(self, value):
        # Insert node at end of list, or create new head node if empty
        if self.head == None:
            new_node = Node(value)
            # self.tail = self.head = new_node
            self.insert_beginning(value)
            return
        else:
            current = self.head
            while current:
                if current.next == None:
                    new_node = Node(value, prev_node=current)
                    current.next = new_node
                    return
                current = current.next

    def insert_beginning(self, value):
        # Insert new node at beginning. Set pointer to current head node
        new_node = None
        if self.head:
            new_node = Node(value, self.head)
            self.head.prev = new_node
            self.head = new_node
        else:
            new_node = Node(value)
            self.head = new_node
        print(f' -- New head node is {value}.')

    def insert_at(self, position, value):
        # Inserts node at specified position. The current node at this position shifts right.
        if position == 0:
            self.insert_beginning(value)
        elif position >= self.length():
            print(f'Unable to insert at position {position}. Max: {self.length() - 1}.')
            return
        else:
            i = 1
            current = self.head.next
            while current:
                if i == position:
                    new = Node(value, current, current.prev)
                    # print(current.prev)
                    current.prev.next = new
                    print(f' -- Inserted {value} at position {i}.')
                    return
                i+=1
                current = current.next
                
    def remove_one(self, value):
        # Removes a node that contains specified value
        current = self.head
        if current.value == value:
            print(' -- Removed head node.')
            self.head = current.next
            return
        else:
            count = 2
            while current:
                next = current.next
                if next and next.value == value:
                    current.next = next.next
                    print(f' -- Removed node number {count} containing {value}.')
                    return 
                count += 1
                current = current.next
        print(f'No nodes with specified value - {value}.')

    def remove_multiple(self, value):
        # Removes nodes that contain specified value
        print(f'\n*** Searching and removing Nodes containing {value}.')
        current = self.head
        count = 0
        # Head contains value?
        while current and current.value == value:
            self.head = current.next
            current = current.next
            count += 1

        while current:
            if current.value != value:
                prev = current
            else:
                prev.next = current.next
                count += 1
            current = current.next
        print(f' -- Removed {count} nodes.\n')
        return

    def remove_at(self, position):
        # Removes node at specified position
        if position == 0:
            self.remove_one(self.head.value)
        elif position >= self.length() or position < 0:
            print(f'Unable to remove at position {position}. Max: {self.length() - 1}.')
        else:
            i = 1
            current = self.head.next
            while current:
                if i == position:
                    
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    print(f' -- Removed node at position {i} containing {current.value}.')
                    return
                i += 1
                current = current.next

   

ll = LinkedList([1, 2, 3, 4, 5, 5, 1, 2, 5])

print(ll.stringify())

ll.insert_beginning(0)

ll.insert_beginning(0)

print(ll.stringify())

if ll.insert_end(100): print(' -- Inserted at end.')

print(ll.stringify())

ll.insert_at(5, 20)

ll.insert_at(20, 10) # error

print(ll.stringify())

print(f'Length of linked list: {ll.length()}')

print(ll.stringify())

ll.remove_one(5)

ll.remove_one(1000) # error

ll.remove_at(1)

ll.remove_at(100) # error

print(ll.stringify())

ll.remove_multiple(5)

ll.remove_multiple(99)

print(ll.stringify())

print(ll)