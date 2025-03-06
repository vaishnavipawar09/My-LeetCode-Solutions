class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, cnt= 0,0

        for n in nums:
            if cnt ==0:
                result=n
            cnt += ( 1 if n == result else -1)
        return result