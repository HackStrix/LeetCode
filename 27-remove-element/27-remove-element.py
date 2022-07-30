class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total = 0
        length = len(nums)
        for i in range(len(nums)):
            # print(nums,i,total)
            if nums[i-total] == val:
                nums.pop(i-total)
                total+=1
        # print(nums)
        return length-total