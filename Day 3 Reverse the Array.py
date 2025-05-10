class Solution:
    def reverseArray(self, arr):
        left = 0
        right = len(arr) - 1
        
        while(left < right):
            arr[left] , arr[right] = arr[right] , arr[left]
            left = left + 1
            right = right - 1