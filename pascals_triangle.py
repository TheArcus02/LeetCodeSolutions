from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []

        def gen(n: int):
            # base case
            if n == 1:
                return [1]

            row = []
            prev_row = gen(n - 1)

            for i in range(n):
                if i == 0 or i == (n - 1):
                    row.append(1)
                else:
                    row.append(prev_row[i - 1] + prev_row[i])
            rows.append(prev_row)
            return row

        rows.append(gen(numRows))

        return rows


def main():
    solution = Solution()
    print(solution.generate(5))


if __name__ == "__main__":
    main()
