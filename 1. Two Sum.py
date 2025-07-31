class Solution(object):
    def twoSum(self, nums, target):
        def mySolution(nums , target):

            hashmap = {}
            
            for indexValues in range(len(nums)):
                realValues = nums[indexValues]
                realvaluesunknownNumber = target - realValues

                if realvaluesunknownNumber in hashmap:
                    return [hashmap[realvaluesunknownNumber] , indexValues]
                else:
                    hashmap[realValues] = indexValues

        return mySolution(nums , target)