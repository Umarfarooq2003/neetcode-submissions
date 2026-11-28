class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1=[]
        nums2=[]
        nums1.append(1)
        for i in range(1,len(nums)):
            value=nums1[i-1]*nums[i-1]
            nums1.append(value)
        nums2.append(1)
        for i in range(len(nums)-2,-1,-1):
            value2=nums2[-1]*nums[i+1]
            nums2.append(value2)
        nums2.reverse()
        for i in range(len(nums)):
            value3=nums1[i]*nums2[i]
            nums[i]=value3
        return nums