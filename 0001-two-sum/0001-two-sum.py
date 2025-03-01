class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map ={}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in h_map:
                return [h_map[diff], i]
            h_map[n] = i
        return 0
        