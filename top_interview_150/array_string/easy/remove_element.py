# question: https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

# solutions:

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # iterate through the array in reverse order
        # so that deletion of an element doesnt not have an effect on the idex of upcomming elements
        # if the element == val, delete the element
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                del nums[i]

        return len(nums)
