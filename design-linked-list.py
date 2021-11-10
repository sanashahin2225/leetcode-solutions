class ListNode:
    def __init__(self,val):
        self.val = val
        self.next= None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index+1):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        self.size += 1
        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
        new_node = ListNode(val)
        new_node.next = ptr.next
        ptr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1
        self.size -= 1
        ptr = self.head
        for _ in range(index):
            ptr = ptr.next
        
        ptr.next = ptr.next.next

