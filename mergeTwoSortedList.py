class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val <= l2.val:
                ptr = l1
                ptr.next = self.mergeTwoLists(l1.next,l2)
            else:
                ptr = l2
                ptr.next = self.mergeTwoLists(l2.next,l1)
                
            return ptr
                
        elif l1 and l2 == None:
            return l1
        elif l2 and l1 == None:
            return l2
        else:
            return None
