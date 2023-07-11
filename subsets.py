from typing import List


class Solution:
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


def main():
    solution = Solution()
    print(solution.subsets([1, 2, 3]))


if __name__ == "__main__":
    main()
