from node import Node

class Queue:
    def __init__(self, max_size=None) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size

    # Return the value of head
    def peek(self):
        if self.head == None:
            print('Queue empty.')
            return
        print(f'Head is {self.head.value}')
        return self.head.value

    def is_empty(self):
        return True if self.size == 0 else False

    def has_space(self):
        if self.max_size:
            return True if self.max_size > self.size else False
        return True

    def get_size(self):
        return self.size

    # Add new node to the back of the queue
    def enqueue(self, value):
        # prevent overflow
        if not self.has_space():
            print('No space in the queue.')
            return
        new = Node(value)
        if self.is_empty():
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.size += 1
        print(f'Added {new.value} to the queue.')
        return new.value

    # Remove a node from the front of the queue (head)
    def dequeue(self):
        # prevent underflow
        if self.is_empty():
            print('Queue empty.')
            return None
        removed = self.head
        print(f'Removing {removed.value} from the queue.')
        if self.get_size() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            print(f'{self.head.value} is new head.')
        self.size -= 1
        return removed.value
        

q = Queue(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.peek()

print(f'Size of queue: {q.get_size()}')

print()
print()

q.dequeue()

print(f'Size of queue: {q.get_size()}')

q.peek()
