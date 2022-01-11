from node import Node

class Stack:
    def __init__(self, max_size = 100) -> None:
        self.top_node = None
        self.size = 0
        self.max_size = max_size

    def peek(self):
        if self.is_empty():
            print('Stack empty.')
            return None
        print(f'Top node is {self.top_node.value}')
        return self.top_node.value

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.max_size > self.size

    def push(self, value):
        if not self.has_space():
            print('Maximum size reached.')
            return
        new = Node(value)
        new.next = self.top_node
        self.top_node = new
        self.size += 1
        print(f'Pushed {new.value}')

    def pop(self):
        if self.is_empty():
            print('Stack empty.')
            return None
        removed = self.top_node
        self.top_node = removed.next
        print(f'Popped {removed.value}')
        self.size -= 1
        return removed.value

    
s = Stack(10)
s.peek()
s.pop()
s.push(1)
s.push(2)
s.push(3)
s.peek()
s.pop()
s.peek()

s2 = Stack(1)
s2.push(1)
s2.push(2)
