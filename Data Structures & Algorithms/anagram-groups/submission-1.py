class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord('a') - ord(c)] += 1
            d[tuple(letters)].append(s)
        return d.values()