class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = {}
        result, maxval= 0,0

        for n in nums:
            val[n] = 1 + val.get(n, 0)
            result = n if val[n]> maxval else result
            maxval = max(val[n], maxval)
        return result