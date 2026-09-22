class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = dict()
        t_dict = dict()
        for ch in s:
            if s_dict.get(ch) == None:
                s_dict.update({ch : 1})
            else:
                s_dict.update({ch : s_dict.get(ch)+1})
        for ch in t:
            if t_dict.get(ch) == None:
                t_dict.update({ch : 1})
            else:
                t_dict.update({ch : t_dict.get(ch)+1})
        return s_dict == t_dict
        