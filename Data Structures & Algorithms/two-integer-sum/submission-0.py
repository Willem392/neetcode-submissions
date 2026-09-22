class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            key = target - nums[i]
            if d.get(key) != None:
                return [d.get(key), i]
            else:
                d.update({nums[i] : i})