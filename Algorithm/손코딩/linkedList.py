class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkedList():
    def __init__(self):
        self.head = None

    def addAtHead(self, value):  # O(1)
        node = Node(value)
        node.next = self.head
        self.head = node

    def addBack(self, value):  # O(n)
        node = Node(value)
        crnt_node = self.head
        while crnt_node.next:
            crnt_node = crnt_node.next
        crnt_node.next = node

    def findNode(self, value):  # O(n)
        crnt_node = self.head
        while crnt_node is not None:
            if crnt_node.value == value:
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError('Node not found')

    def addAfter(self, node: Node, value):  # O(1)
        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def deleteAfter(self, prev_node: Node):  # O(1)
        if prev_node.next is not None:
            prev_node.next = prev_node.next.next


def printNodes(node: Node):
    crnt_node = node

    while crnt_node is not None:
        print(crnt_node.value, end=' ')
        crnt_node = crnt_node.next


slist = SLinkedList()
slist.addAtHead(1)
slist.addAtHead(2)
slist.addBack(3)

node1 = slist.findNode(1)
slist.addAfter(node1, 4)
slist.deleteAfter(node1)

printNodes(slist.head)
# head_node = Node(1)
# head_node.next = Node(2)
# head_node.next.next = Node(3)
# head_node.next.next.next = Node(4)


# printNodes(head_node)
