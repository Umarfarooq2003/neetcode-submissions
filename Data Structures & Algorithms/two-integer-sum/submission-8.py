class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        freq={}
        for right in range(len(nums)):
            needed=target-nums[right]
            if needed in freq:
                return [freq[needed],right]
            freq[nums[right]]=right