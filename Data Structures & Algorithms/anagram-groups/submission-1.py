class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        res = []

        for word in strs:
            mp[''.join(sorted(word))].append(word)

        for key,value in mp.items():
            res.append(value)

        return res