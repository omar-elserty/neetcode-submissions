class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i,j in enumerate(nums):
            dict1[j]=i

        for i in range(len(nums)):
            difference = target - nums[i]
            

            if(difference in dict1 and i != dict1[difference]):
                return [i,dict1[difference]]

            

            

        