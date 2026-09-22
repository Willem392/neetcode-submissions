class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [nums[0]] * len(nums)
        post = [nums[-1]] * len(nums)
        output = []
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i]
            post[-i-1] = post[-i] * nums[-i-1]
        pre.insert(0, 1)
        post.insert(len(nums), 1)
        for i in range(1, len(nums)+1):
            output.append(pre[i-1]*post[i])
        return output