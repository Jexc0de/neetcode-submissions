class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        r = []
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        return list(freq.keys())[:k]