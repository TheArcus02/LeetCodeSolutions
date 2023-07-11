from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Implemntation for array data structure
    """

    def invertTree_(self, root: List[int]) -> List[int]:
        if len(root) != 0:
            new_root = root[:]
            for i in range(len(root) // 2):
                rt = new_root[i]
                l, r = ((root.index(rt) + 1) * 2) - 1, (root.index(rt) + 1) * 2
                l_, r_ = ((i + 1) * 2) - 1, (i + 1) * 2

                new_root[r_], new_root[l_] = root[l], root[r]
            return new_root
        return root

    """
    Implmentation for TreeNode data structure
    """

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root


def main():
    solution = Solution()
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(9)

    print(solution.invertTree(tree))


if __name__ == "__main__":
    main()
