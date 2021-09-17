class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        ptr = head
        while ptr != None:
            count += 1
            ptr = ptr.next
        if n> count:
            return head;
        elif count == n:
            head = head.next
        else:
            ptr = head
            for i in range(count-n-1):
                ptr = ptr.next
            ptr.next = ptr.next.next
        return head
