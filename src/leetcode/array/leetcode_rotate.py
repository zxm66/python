class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        size = len(matrix)

        for i in range(size/2):
            for j in range(size /2):
                tmp =matrix[i][j]
                matrix[i][j] = matrix[size -1 - i][j]
                matrix[size - 1-i][j] = matrix[size - 1 - i][size -1  -j]
                matrix[size - 1 - i][size -1 -j] = matrix[i][size -1 -j]
                matrix[i][size -1 -j] = tmp

if __name__ == "__main__":
    matrix = [[1,2,3],[1,2,3],[1,2,3]]
    Solution().rotate(matrix)
    print (matrix)
    print (matrix[1][1])


