from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        inorder = list()

        inorder.extend(self.inorderTraversal(root.left))
        inorder.append(root.val)
        inorder.extend(self.inorderTraversal(root.right))

        return inorder


def main():
    solution = Solution()
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)

    print(solution.inorderTraversal(tree))


if __name__ == "__main__":
    main()
