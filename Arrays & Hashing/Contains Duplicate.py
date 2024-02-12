# https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        for num in nums:
            isPresent = lookup.get(num, False)
            if isPresent:
                return True
            lookup[num] = True
        return False
        
# Set is preferred since we save some memory
