class Solution:
    def getSecondLargest(self, arr):
        n = len(arr)
        if n < 2:
            return -1
    
        fmax = smax = float('-inf')
        
        for num in arr:
            if num > fmax:
                smax = fmax
                fmax = num
            elif num > smax and num < fmax:
                smax = num
        
        if smax == float('-inf'):
            return -1
        else:
            return smax