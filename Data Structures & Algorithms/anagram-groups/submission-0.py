class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for ch in s:
                chars[ord(ch)-ord('a')] += 1
            d[tuple(chars)].append(s)
        return d.values()