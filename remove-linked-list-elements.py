# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    
        if not head:
            return None
         
        if head and head.next:
            ptr = head.next
            prev = head
            
            while ptr != None:
                if prev.val == val and head == prev:
                    prev = ptr
                    head = prev
                    ptr = ptr.next
                elif ptr.val == val:
                    ptr = ptr.next
                    prev.next = ptr
                else:
                    prev = ptr
                    ptr = ptr.next
        
        if head.val == val:
            return None
        
        return head
