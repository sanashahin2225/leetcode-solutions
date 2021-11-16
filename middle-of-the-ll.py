class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def counter(head):
            ptr = head
            count = 0
            
            while ptr:
                count += 1
                ptr = ptr.next
             
            return count
        
        tmp = counter(head)
        
        val = tmp//2
        ptr = head
        while val:
            ptr = ptr.next
            val -= 1
        return ptr
