# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
            def rootCheck(root):
                if not root: return [] # root가 비어있지 않다면 빈 리스트를 반환

                if not root.left and not root.right: # root의 왼쪽과 오른쪽가지 모두 비어있지 않다면
                    return [root.val] # root.val 을 반환

                return rootCheck(root.left) + rootCheck(root.right) # 왼쪽과 오른쪽 다 더해서 비교
            return rootCheck(root1) == rootCheck(root2)

        

        
