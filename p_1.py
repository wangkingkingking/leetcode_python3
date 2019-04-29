class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val2idx = {v:k for k, v in enumerate(nums)}
        #print(val2idx)
        for k, v in enumerate(nums):
            if target - v in val2idx:
                if k != val2idx[target-v]:
                    return [k, val2idx[target-v]]
