class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import Counter

        anagram_dict = defaultdict(list)

        for s in strs:
            anagram_dict[tuple(sorted(Counter(s).items()))].append(s)
        
        return list(anagram_dict.values())

        