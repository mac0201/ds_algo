class Node:
    def __init__(self, value, next_node=None) -> None:
        self.value = value
        self.next = next_node

    def __repr__(self) -> str:
        return str(self.value)