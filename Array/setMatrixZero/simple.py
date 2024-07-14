class Solution:
    def setZeroes(self, nums: List[int]) -> None:
        if not nums or not nums[0]:
            return
        
        count_rows_zeros = set()
        count_cols_zeros = set()
        # use set to fix the (i,j)th index to zero, and then zero all those which fall in this bracket.
        rows = len(nums)
        cols = len(nums[0])

        for i in range(rows):
            for j in range(cols):
                if nums[i][j] == 0:
                    count_rows_zeros.add(i)
                    count_cols_zeros.add(j)

        for i in range(rows):
            for j in range(cols):
                if i in count_cols_zeros or j in count_rows_zeros:
                    nums[i][j] = 0

        return nums
