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


def main():
    solution = Solution()
    # print(solution.twoSum([-1, -2, -4, -5], -9))
    # print(solution.romanToInt("MCMXCIV"))
    print(solution.longestCommonPrefix(["reflower", "flow", "flight"]))


if __name__ == "__main__":
    main()
