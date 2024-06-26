class Solution:
    def containsDuplicate(self, nums) -> bool:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                return True
            num_dict[num] = True
        return False
