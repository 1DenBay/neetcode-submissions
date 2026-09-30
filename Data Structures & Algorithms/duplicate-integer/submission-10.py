class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # I started a set to ensure the numbers do not repeat 

        for i in nums: # a loop to check the numbers in the set one by one
            if i in hashset: # i checked nums in the set
                return True
            hashset.add(i)
        return False