class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        m = A[0]
        tempMax = A[0]

        for num in A[1:]:
            tempMax = max(num, tempMax + num)
            m = max(m, tempMax)

        return m
