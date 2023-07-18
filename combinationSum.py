from typing import List

"""
idea code
comb_counter = 0
        combs = []
        cur_sum = 0
        curr_comb = []
        for num in candidates:
            if num > target:
                candidates.remove(candidates[num])
                continue
            
            elif cur_sum + num < target:
                cur_sum += num
                curr_comb.append(num)
            elif cur_sum + num == target:
                cur_sum = 0
                curr_comb.append(num)
                combs.append(curr_comb)
                curr_comb = []
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking?
        combs = []
        stack = []

        def backtrack(curr_sum, nums):
            if curr_sum == target:
                combs.append(stack.copy())
                return

            for i in range(len(nums)):
                if curr_sum + nums[i] <= target:
                    stack.append(nums[i])
                    backtrack(curr_sum + nums[i], nums[i:])
                    stack.pop()

        backtrack(0, candidates)
        return combs


def main():
    solution = Solution()
    print(solution.combinationSum([2, 3, 6, 7], 7))


if __name__ == "__main__":
    main()
