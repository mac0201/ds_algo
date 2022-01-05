# Create a node
class Node_old:
    def __init__(self, value, next_node = None) -> None:
        self.value = value
        self.next_node = next_node

    # get node's value
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    # Set next node
    def set_next_node(self, next_node):
        self.next_node = next_node


class Node:
    def __init__(self, value, next_node=None, prev_node=None) -> None:
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __repr__(self) -> str:
        return str(self.value)