from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or base[i] != word[i]:
                    return base[:i]
        return base


def main():
    solution = Solution()
    print(solution.longestCommonPrefix(["reflower", "flow", "flight"]))


if __name__ == "__main__":
    main()
