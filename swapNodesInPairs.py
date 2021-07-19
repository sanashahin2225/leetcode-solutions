class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head != None:
            if head.next == None:
                return head # If only one element exists
            else:
                ptr1 = head
                ptr2 = head.next
                if ptr1.next == None:
                    temp = ptr1.val
                    ptr1.val = ptr2.val
                    ptr2.val = temp
                    
                    return head # if two element exists
                else:
                    while ptr1.next != None:
                        temp = ptr1.val
                        ptr1.val = ptr2.val
                        ptr2.val = temp
                        
                        if ptr2.next == None:
                            break
                            
                        ptr1 = ptr2.next
                        ptr2 = ptr2.next.next
                    return head
        else:
            return head
