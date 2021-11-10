
        l = []
        while head:
            l.append(head.val)
            head = head.next
        k = l[left-1:right]
        list1 = l[:left-1] + k[::-1] + l[right:]
        curr = dummy = ListNode(0)
        for i in list1:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
