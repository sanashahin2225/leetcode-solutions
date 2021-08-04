class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        
        def preorder(root):
            if root != None:
                ans.append(root.val)
                preorder(root.left)
                preorder(root.right)
            
        preorder(root)
        return ans
