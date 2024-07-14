def removeDuplicates(self, nums: List[int]) -> int:
        sort = set()
        for num in nums:
            sort.add(num)        
        return (len(sort), list(sort))
