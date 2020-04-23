class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for index, value in enumerate(nums):
            remain = target - value
            if remain in check:
                return [check[remain], index]
            check[value] = index
        return []
                
