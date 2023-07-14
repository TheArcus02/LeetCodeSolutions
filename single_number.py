from typing import List


class Solution:
    # Hash set solution
    # O(n) runtime complexity
    # O(n) space complexity
    def singleNumber_one(self, nums: List[int]) -> int:
        mapping = []
        for num in nums:
            if not num in mapping:
                mapping.append(num)
            else:
                mapping.remove(num)
        return mapping[0]

    # XOR solution
    # O(n) runtime complexity
    # O(1) space complexity
    def singleNumber_two(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res


def main():
    solution = Solution()
    print(solution.singleNumber_one([4, 1, 2, 1, 2]))
    print(solution.singleNumber_two([4, 1, 2, 1, 2]))


if __name__ == "__main__":
    main()
