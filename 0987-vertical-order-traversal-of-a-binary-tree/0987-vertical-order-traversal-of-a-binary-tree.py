# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d=defaultdict(lambda :defaultdict(list))
        q=deque([(0,0,root)])
        while len(q)>0:
            level,vertical,node=q.popleft()
            if(node.left):
                q.append([level+1,vertical-1,node.left])
            if(node.right):
                q.append([level+1,vertical+1,node.right])
            d[vertical][level].append(node.val)
        ans=[]
        for i in sorted(d):
            temp=[]
            for j in sorted(d[i]):
                temp.extend(sorted(d[i][j]))
            ans.append(temp)
        return ans
        