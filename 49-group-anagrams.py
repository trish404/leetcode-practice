from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            c = [0] * 26
            for char in s:
                c[ord(char)-ord('a')] += 1
            
            groups[tuple(c)].append(s)
        
        return list(groups.values())
