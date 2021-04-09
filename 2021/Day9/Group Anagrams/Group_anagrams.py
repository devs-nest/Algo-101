class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequencies = dict()
        for s in strs:
            key = ''.join(sorted(s))
            try:
                frequencies[key].append(s)
            except:
                frequencies[key] = [s]
        return list(frequencies.values())
