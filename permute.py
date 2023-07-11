from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 or len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            new_perm = nums.copy()
            new_perm[0], new_perm[1] = new_perm[1], new_perm[0]
            return [nums, new_perm]

        permutations = []
        for i in range(len(nums)):
            for perm in self.permute(nums[:i] + nums[i + 1 :]):
                permutations.append([nums[i]] + perm)
        return permutations


def main():
    solution = Solution()
    print(solution.permute([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
