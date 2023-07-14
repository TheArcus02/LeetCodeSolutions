from typing import List


class Solution:
    # recursion aproach
    def generate_one(self, numRows: int) -> List[List[int]]:
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

    # iterative aproach (better)
    def generate_two(self, numRows: int) -> List[List[int]]:
        results = [[1]]

        for i in range(numRows - 1):  # -1 becouse first row is already added
            prev = [0] + results[-1] + [0]
            row = []
            for j in range(len(results[-1]) + 1):  # new row size is going to be last row + 1
                row.append(prev[j] + prev[j + 1])
            results.append(row)
        return results


def main():
    solution = Solution()
    print(solution.generate_one(5))
    print(solution.generate_two(5))


if __name__ == "__main__":
    main()
