from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            p, q = nums[r], l
            for i in range(l, r):
                if nums[i] <= p:
                    nums[q], nums[i] = nums[i], nums[q]
                    q += 1
            nums[q], nums[r] = nums[r], nums[q]

            if q > k:
                return quickSelect(l, q - 1)
            elif q < k:
                return quickSelect(q + 1, r)
            else:
                return nums[q]

        return quickSelect(0, len(nums) - 1)


def main():
    solution = Solution()
    print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))


if __name__ == "__main__":
    main()
