class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        if len(A) in [0, 1]:
            return 0
        x = A[0]
        y = B[0]
        dist = 0
        for i in range(1, len(A)):
            distX = abs(A[i] - x)
            distY = abs(B[i] - y)
            x = A[i]
            y = B[i]
            dist += max(distX, distY)
        return dist
