class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid 
                break 
            elif nums[mid] < target:
                left = mid + 1  
            else:
                right = mid - 1  
        return index  