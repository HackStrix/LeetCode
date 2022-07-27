class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        y = len(nums)-1
        while nums[i]+nums[y]!=target:
            if nums[i]+nums[y] > target:
                y-=1
            else:
                i+=1
        return [i+1,y+1]