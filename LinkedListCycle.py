class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ptr = head
        dic = set()
        if not head:
            return None
        while ptr:
            if ptr in dic:
                return ptr
            else:
                dic.add(ptr)
            
            ptr = ptr.next
        return None
