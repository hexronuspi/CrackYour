class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        num_non = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[num_non] = nums[i]
                num_non += 1
        
        for i in range(num_non,len(nums)):
            nums[i] = 0

        return nums
        

            
