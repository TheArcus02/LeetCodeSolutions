from typing import List


class Solution:
    # Rotations aproach

    def rotate_one(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l <= r:  # while l<r do rotations
            for i in range(r - l):
                t, b = l, r

                temp = matrix[t][l + i]

                matrix[t][l + i] = matrix[b - i][l]
                matrix[b - i][l] = matrix[b][r - i]
                matrix[b][r - i] = matrix[t + i][r]
                matrix[t + i][r] = temp
            r -= 1
            l += 1

    # Reverse than transpose the matrix aproach
    def rotate_two(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        n = len(matrix)

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def main():
    solution = Solution()
    matrix_one = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_two = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate_one(matrix_one)
    solution.rotate_two(matrix_two)
    print(matrix_one)
    print(matrix_two)


if __name__ == "__main__":
    main()
