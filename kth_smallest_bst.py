from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            if node.left:
                inorder(node.left)
            traversal.append(node.val)
            if node.right:
                inorder(node.right)
            return

        inorder(root)
        return traversal[k - 1]


def main():
    solution = Solution()
    tree = TreeNode(3)
    tree.left = TreeNode(1)
    tree.left.right = TreeNode(2)
    tree.right = TreeNode(4)
    print(solution.kthSmallest(tree, 1))


if __name__ == "__main__":
    main()
