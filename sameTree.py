class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p != None and q != None:
            if p.val == q.val:
                return(self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
            else:
                return False
        elif p == None and q == None:
            return True
        else:
            return False
