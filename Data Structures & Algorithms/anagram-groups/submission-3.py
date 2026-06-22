class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import Counter

        anagram_dicts = defaultdict(list)

        for s in strs:
            dict_key = tuple(sorted(Counter(s).items()))
            anagram_dicts[dict_key].append(s)
        
        return list(anagram_dicts.values())
        