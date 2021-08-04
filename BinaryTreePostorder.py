class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        
        def postorder(root):
            if root != None:
                
                postorder(root.left)
                postorder(root.right)
                ans.append(root.val)
            
        postorder(root)
        return ans
