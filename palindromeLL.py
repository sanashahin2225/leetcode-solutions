class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        lst = []
        
        def pal(head):
            if head.next == None:
                lst.append(head.val)
                return lst
            else:
                lst.append(head.val)
                return pal(head.next)
            
        def lsttostr(a):
            str1 = ''
            for ele in a:
                str1 += str(ele)
            return str1
        
        if head:
            a = pal(head)
            value = lsttostr(a)
            if value == value[::-1]:
                return True
            else:
                return False
