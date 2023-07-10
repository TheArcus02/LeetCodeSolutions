from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in num_dict:
                return [num_dict[x], i]
            num_dict[nums[i]] = i
        return None

    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        for i in range(len(s)):
            if i + 1 < len(s) and mapping[s[i]] < mapping[s[i + 1]]:
                number -= mapping[s[i]]
            else:
                number += mapping[s[i]]
        return number

    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or base[i] != word[i]:
                    return base[:i]
        return base

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 or len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            new_perm = nums.copy()
            new_perm[0], new_perm[1] = new_perm[1], new_perm[0]
            return [nums, new_perm]

        permutations = []
        for i in range(len(nums)):
            print("-----------------pemutation-----------------")
            print("i: ", i)
            print(nums)
            print(self.permute(nums[:i] + nums[i + 1 :]))
            for perm in self.permute(nums[:i] + nums[i + 1 :]):
                permutations.append([nums[i]] + perm)
        return permutations

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     interval = range(len(nums))
    #     subsets = [nums]
    #     for curr_interval in interval:
    #         for i in range(len(nums) + 1):
    #             next_subset = nums[i : i + curr_interval]
    #             if next_subset not in subsets:
    #                 subsets.append(next_subset)
    #     return subsets
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums, []]

        subs = [nums]

        for i in range(len(nums)):
            for sub in self.subsets(nums[:i] + nums[i + 1 :]):
                if sub not in subs:
                    subs.append(sub)
        return subs

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
    # print(solution.twoSum([-1, -2, -4, -5], -9))
    # print(solution.romanToInt("MCMXCIV"))
    # print(solution.longestCommonPrefix(["reflower", "flow", "flight"]))
    # print(len(solution.permute([1, 2, 3, 4])))
    # print(solution.subsets([1, 2, 3]))
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
