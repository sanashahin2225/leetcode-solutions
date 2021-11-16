def dfs(head,root):
            if not head:
                return True
            if not root:
                return False
            return root.val == head.val and (dfs(head.next,root.left) or dfs(head.next,root.right))
        
        
        if not head:
            return True
        if not root:
            return False
        if root.val == head.val and dfs(head,root):
            return True
        return self.isSubPath(head,root.left) or self.isSubPath(head,root.right)
