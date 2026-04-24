class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import Counter
        anagrams_dict = defaultdict(list)
        for strng in strs:
            key = tuple(sorted((Counter(strng).items())))
            anagrams_dict[key].append(strng)

        # print(list(anagrams_dict.values()))
        return list(anagrams_dict.values())


        