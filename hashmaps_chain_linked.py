from node import Node
# This hash map implementation uses the chaining strategy with Linked List to deal with hash collisions


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current:
            if current.next:
                current = current.next
            current.next = new_node
            return

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


class HashMap:
    def __init__(self, max_size):
        self.MAX = max_size
        self.array = [LinkedList() for i in range(max_size)]

    def hash(self, key):  # + compress
        hash_value = sum(key.encode())
        return hash_value % self.MAX

    def add(self, key, value):
        index = self.hash(key)
        current_list = self.array[index]
        for item in current_list:
            if item[0] == key:
                print('update')
                item[1] = value
                return
        print('add new')
        new = Node([key, value])
        current_list.insert(new)

    def get(self, key):
        index = self.hash(key)
        current_list = self.array[index]
        for item in current_list:
            if item[0] == key:
                return item[1]
        return None


map = HashMap(1)

map.add('key1', 'val1')
map.add('key2', 'val2')
map.add('key3', 'val3')
map.add('key2', 'val2new')

print(map.get('key2'))
