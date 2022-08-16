class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


head_node = Node(1)
head_node.next = Node(2)
head_node.next.next = Node(3)
head_node.next.next.next = Node(4)


def printNodes(node: Node):
    crnt_node = node

    while crnt_node is not None:
        print(crnt_node.value, end=' ')
        crnt_node = crnt_node.next


printNodes(head_node)
