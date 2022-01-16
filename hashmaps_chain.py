# This hash map implementation uses the chaining strategy to deal with hash collisions
class HashMap:
    def __init__(self, max_size):
        self.MAX = max_size
        self.array = [[] for i in range(max_size)]

    def hash(self, key):
        hash_value = sum(key.encode())
        return hash_value % self.MAX

    def add(self, key, value):
        index = self.hash(key)
        current = self.array[index]
        # if not current:
        #     # append to the array
        #     print(f'added at {index}')
        #     current.append([key, value])
        #     return
        for idx, ele in enumerate(current):
            if ele[0] == key:
                current[idx] = [key, value]
                return
        current.append([key, value])

    def get(self, key):
        index = self.hash(key)
        current = self.array[index]
        for element in current:
            if element[0] == key:
                return element[1]
        return None

    def delete(self, key):
        index = self.hash(key)
        current = self.array[index]
        deleted = None
        for idx, element in enumerate(current):
            if element[0] == key:
                deleted = element
                del current[idx]
                return deleted
        print('Element not found')
        return None


# hash + compress
# add -> __setitem__
# get -> __getitem__
# delete -> __delitem__
# each index in the internal array will hold empty array
# values are saved to empty array
# if two different keys have same hash, save both in the array at given index
map = HashMap(10)
map.add('key1', 'val1')
map.add('key2', 'val2')
map.add('key3', 'val3')
map.add('key4', 'val4')
map.add('key4', 'va11111')
map.add('ke1y', 'va111555')
map.add('k1ey', 'va111')

print(map.array)
print(len(map.array))


print(map.get('key3'))


x = map.delete('k1ey')
print(x)

print(map.array)
