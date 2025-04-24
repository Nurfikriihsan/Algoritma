class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.is_marked = False
        self.next = self
        self.prev = self

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0

    def insert(self, key):
        new_node = Node(key)
        if not self.min_node:
            self.min_node = new_node
        else:
            self._link(self.min_node, new_node)
            if new_node.key < self.min_node.key:
                self.min_node = new_node
        self.num_nodes += 1

    def _link(self, min_node, new_node):
        new_node.prev = min_node.prev
        new_node.next = min_node
        min_node.prev.next = new_node
        min_node.prev = new_node

    def find_min(self):
        return self.min_node.key if self.min_node else None

    def extract_min(self):
        pass

    def union(self, other_heap):
        pass

fib_heap = FibonacciHeap()
fib_heap.insert(10)
fib_heap.insert(5)
print(fib_heap.find_min())  