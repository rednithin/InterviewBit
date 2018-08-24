class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        sub = []
        temp = []
        for elem in A:
            if elem < 0:
                sumTemp = sum(temp)
                sumSub = -1 if len(sub) == 0 else sum(sub)
                if sumTemp > sumSub:
                    sub = temp[:]
                elif sumTemp == sumSub and len(temp) > len(sub):
                    sub = temp[:]
                temp = []
            else:
                temp.append(elem)
        sumTemp = sum(temp)
        sumSub = sum(sub)
        if sumTemp > sumSub:
            sub = temp[:]
        elif sumTemp == sumSub and len(temp) > len(sub):
            sub = temp[:]
        return sub
