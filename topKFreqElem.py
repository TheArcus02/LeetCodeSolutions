from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        return sorted(dictionary, key=dictionary.get, reverse=True)[:k]

def main():
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums, k))

main()