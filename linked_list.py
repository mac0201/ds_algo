from node import Node

# Singly linked list
class LinkedList:
    def __init__(self, values=None) -> None:
        self.head = None
        self.tail = None
        self.value = None
        if values is not None:
            self.insert_multiple_end(values) if type(values) is list else self.insert_one_beginning(values)
            
    def get_total_nodes(self):
        count = 0
        current = self.head
        while current:
            count+=1
            current = current.next
        return count

    def get_head_node(self):
        return self.head.value if self.head else None

    def get_tail_node(self):
        return self.tail.value if self.tail else None

    def stringify(self):
        current = self.head
        string = ''
        while current:
            string += str(current.value) + ' -> ' if current.next else str(current.value)
            current = current.next
        print(string)

    def insert_head(self, value, next=None):
        new = Node(value, next)
        self.tail = self.head = new
        print(" -- New head node set.")
        return new

    def insert_one_beginning(self, value):
        if self.head == None:
            self.insert_head(value)
        else:
            new = Node(value, self.head)
            self.head = new

    def insert_multiple_beginning(self, values):
        for value in values:
            self.insert_one_beginning(value)
        print(f' -- Inserted {len(values)} values at start.')

    def insert_one_end(self, value):
        if self.head == None:
            self.insert_head(value)
        else:
            new = Node(value)
            self.tail.next = new
            self.tail = new

    def insert_multiple_end(self, values):
        for value in values:
            self.insert_one_end(value)
        print(f' -- Inserted {len(values)} values at end.')

    def insert_at_position(self, position, value):
        if self.head == None:
            self.insert_head(value)
            return value
        new_node = Node(value)
        if position == 0:
            self.insert_head(value, self.head)
        elif position > self.get_total_nodes():
            print(f'Specified position out of bounds. Added "{value}" as tail instead.')
            self.insert_one_end(value)
        else:
            current = self.head
            i = 0
            while current:
                if (i + 1) == position:
                    new_node.next = current.next
                    current.next = new_node
                    print(f' -- Inserted {value} at position {position}')
                    return
                i += 1
                current = current.next
 
    def insert_after_value(self, target_value, value):
        current = self.head
        i = 0
        while current:
            if current.value == target_value:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                print(f' --  Inserted {value} after target: {target_value}.  Position - {i + 1}')
                return
            i += 1
            current  = current.next
        print('Could not find specified value.')

    def remove_current_head(self):
        head = self.head
        if head == None:
            print('List empty.')
            return
        if head.next:
            print(f' -- Removed current head ({head.value}) and set {head.next.value} as new head.')
            self.head = head.next
        else:
            print(f' -- Removed current head, which was the only node. List now empty.')
            self.head = None

    def remove_current_tail(self):
        if self.tail == self.head:
            print('Tail is head. Remove cancelled.')
            return
        current = self.head
        while current.next.next:
            current = current.next
        print(f' -- Removed current tail node ({self.tail.value}) and set {current.value} as new tail node.')
        current.next = None
        self.tail = current

    def remove_node(self, value):
        if self.head.value == value:
            print(' -- Head node contains value.')
            self.remove_current_head()
        else:
            current = self.head
            while current:
                next = current.next
                if next and next.value == value:
                    if next == self.tail:
                        self.tail = current
                    print(' -- Found and removed')
                    current.next = next.next
                    return
                current = current.next
            print('Value not found')
            return

    def remove_multiple_nodes(self, value):
        current = self.head
        count = 0
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
        print(f' -- Removed {count} node(s) with value of {value}' if count else f'No nodes with value of {value} found.')
    
    def sort(self):
        current = self.head
        index = None
        if current is None:
            print('Unable to sort empty list.')
            return
        else:
            while current:
                index = current.next
                while index:
                    if (type(index.value) == float) or (type(index.value) == int):
                        if current.value > index.value:
                            temp = current.value
                            current.value = index.value
                            index.value = temp
                        index = index.next
                    else:
                        print('List contains elements of type other than numbers.  Unable to sort.')
                        return
                current = current.next
            print(' -- List sorted.')

    def remove_at_position(self, position: int):
        if type(position) is not int or position < 0 or position >= self.get_total_nodes():
            print('Invalid position.')
            return

        if position == 0:
            self.remove_current_head()
            return

        if position == self.get_total_nodes() - 1:
            self.remove_current_tail()
            return
        
        current = self.head
        prev = None
        i = 0
        while current:
            if i == position:
                prev.next = current.next
                print(f' -- Removed node cotaining {current.value} from position {position}')
                return
            i+=1
            prev = current
            current = current.next

    def remove_after_value(self, target):
        current = self.head
        count = 0
        while current:
            if current.value == target:
                print(f' -- Found target value {target} at position {count}. Removed next node containing {current.next.value}.')
                current.next = current.next.next
                return
            count += 1
            current = current.next
        print('Value not found.')

    def swap(self, val1, val2):
        node1 = self.head
        node2 = self.head
        node1_prev = None
        node2_prev = None

        if val1 == val2:
            print('Values are the same. No swapping.')
            return

        # Loop through the list 
        # If node's value == value break out of the loop
        # If not, node's previous to current node, and go to next node
        while node1:
            if node1.value == val1:
                break
            node1_prev = node1
            node1 = node1.next

        while node2:
            if node2.value == val2:
                break
            node2_prev = node2
            node2 = node2.next

        if (node1 == None or node2 == None):
            print('One of the values not found.')
            return

        print(f' -- Swapping {val1} with {val2}')

        # Take care of pointers TO swapped nodes
        # If node's previous is None it means that the node is the head. In this case, set head to be the other node (n1 -> n2, n2 -> n1)
        # else set node_previous next to be the other node (n1.prev.next -> n2 / n2.prev.next -> n1)
        if node1_prev == None:
            self.head = node2
        else:
            node1_prev.next = node2


        if node2_prev == None:
            self.head = node1
        else:
            node2_prev.next = node1


        # Take care of pointers FROM swapped nodes
        temp = node1.next
        node1.next = node2.next
        node2.next = temp

        print(' -- Swap done.')



ll = LinkedList([1, 2, 14, 3.3, 3, 4, 10])

ll.insert_one_beginning(5)

ll.insert_one_end(15)

ll.insert_one_end(150)

ll.stringify()

ll.insert_at_position(5, 12)

ll.remove_current_tail()

ll.stringify()

ll.sort()

ll.stringify()

ll.swap(5, 14)

ll.stringify()

print('Total nodes: ' + str(ll.get_total_nodes()))
