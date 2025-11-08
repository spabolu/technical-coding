# 1.7
# runtime: O(M*N)
# spacetime: O(1)
def solution(matrix: list[list[int]]) -> list[list[int]]:
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in range(len(matrix)):
        matrix[row] = matrix[row][::-1]

    return matrix

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # [[7, 4, 1], [8, 5, 2], [9, 6, 3]
print(solution([ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], ])) # [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]
