class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftHead, rightHead = ListNode(), ListNode()
        leftTail, rightTail = leftHead, rightHead

        while head:
            if head.val < x:
                leftTail.next = head 
                leftTail = leftTail.next 
            else:
                rightTail.next = head 
                rightTail = rightTail.next 
            head = head.next 

        leftTail.next = rightHead.next 
        rightTail.next = None 

        return leftHead.next
