from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        stack = []

        def backtrack(opened, closed):
            if opened == closed == n:
                results.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return results


def main():
    solution = Solution()
    print(solution.generateParenthesis(3))


if __name__ == "__main__":
    main()
