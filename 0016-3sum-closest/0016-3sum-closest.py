class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        i = 0
        for i in range(len(nums) - 2):
            l, r = i +1, len(nums) - 1
            while l< r:
                calsum = nums[i] + nums[l] + nums[r]
                if abs(calsum - target) < abs(closest - target):
                    closest = calsum
                if calsum < target:
                    l += 1
                elif calsum > target:
                    r -= 1
                else:
                    return calsum
        return closest

        