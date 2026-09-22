class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence = [ [] for _ in range(len(nums)) ]
        d = {}
        for i in nums:
            d[i] = d.get(i, -1) + 1
        for v in d:
            occurence[d[v]].append(v)
        res = []
        for i in range(len(occurence) - 1, -1, -1):
            for n in occurence[i]:
                res.append(n)
                if len(res) == k:
                    return res