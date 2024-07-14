import numpy as np
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = np.array(nums)
        unique, counts = np.unique(arr, return_counts=True)a
        for value, count in zip(unique, counts):
            if count>1:
              return value

                    
