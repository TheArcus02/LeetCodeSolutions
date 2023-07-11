from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in num_dict:
                return [num_dict[x], i]
            num_dict[nums[i]] = i
        return None


def main():
    solution = Solution()
    print(solution.twoSum([-1, -2, -4, -5], -9))


if __name__ == "__main__":
    main()
