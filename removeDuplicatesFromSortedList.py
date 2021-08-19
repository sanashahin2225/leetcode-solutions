class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head:
            ptr2 = head.next
            
            ptr1 = head
            
            while ptr2 != None:
                
                if ptr1.val == ptr2.val:
                    ptr1.next = ptr2.next
                    ptr2 = ptr2.next
                else:
                    ptr1 = ptr2
                    ptr2 = ptr2.next

            return head
        else:
            return None
