# This hash map implementation uses the open addressing strategy to deal with hash collisions
class HashMap:
    def __init__(self, max_size) -> None:
        self.MAX = max_size
        self.array = [None for i in range(max_size)]

    def hash(self, key, num_col=0):
        hash_value = sum(key.encode()) + num_col
        return hash_value % self.MAX

    def add(self, key, value):
        index = self.hash(key)
        current = self.array[index]
        if current == None:
            print('free spot')
            self.array[index] = [key, value]
            return
        if current[0] == key:
            print('update spot')
            self.array[index][1] = value
            return
        collisions = 1
        while current[0] != key and collisions <= self.MAX:
            print('what')
            index = self.hash(key, collisions)
            current = self.array[index]
            if not current:
                self.array[index] = [key, value]
                return
            if current[0] == key:
                self.array[index] = [key, value]
                return
            collisions += 1
        return

    def get(self, key):
        index = self.hash(key)
        current = self.array[index]
        if current == None:
            return None
        if current[0] == key:
            return current[1]

        collisions = 1
        while current[0] != key and collisions <= self.MAX:
            print(f'COLLISIONS: {collisions}')
            index = self.hash(key, collisions)
            print(f'new index = {index}')
            current = self.array[index]
            if current == None:
                return None
            if current[0] == key:
                return current[1]
            collisions += 1
        return None

    def delete(self, key):
        index = self.hash(key)
        current = self.array[index]
        removed = None
        if not current:
            print('Not found.')
            return removed

        if current[0] == key:
            removed = current
            self.array[index] = None
            return removed

        # collision
        collisions = 1
        while current[0] != key:
            index = self.hash(key, collisions)
            current = self.array[index]
            if not current:
                return removed
            if current[0] == key:
                removed = current
                self.array[index] = None
                return removed
            collisions += 1
        return None


map = HashMap(5)

map.add('282', 'hello')
map.add('228', 'helloz')
map.add('882', 'welcome')
map.add('e4', 'da')
map.add('what', 'here')
# map.add('fia', 'asdi')


# print(map.get('282'))
# print(map.get('228'))
# print(map.get('whioefhiodfhdiat'))

print(map.array)


map.delete('282')

print(map.array)


map.add('hfa2', 'aisdha2')


print(map.array)
