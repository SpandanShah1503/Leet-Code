class Solution:
    def searchRange(self, nums, target):

        def findingFirstIndex(nums, target):
            left = 0
            right = len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    index = mid
                    
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return index

        def findingSecondIndex(nums, target):
            left = 0
            right = len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    index = mid
                    
                    left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return index

        return [findingFirstIndex(nums, target), findingSecondIndex(nums, target)]