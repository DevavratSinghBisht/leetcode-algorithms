# question : https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

# solution

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # iterator for num1 and num2
        i = 0
        j = 0


        # strategy is to place num2's element before num1's element
        # whenever num1s element is greater than num2's
        # this condition is in the third condition
        while True:

            # if all the eleemnts of num1 has been seen
            # simply place rest of the num2 elements towards the end of num1 elements
            if i == m+j:
                for k in range(j, len(nums2)):
                    nums1[m+k] = nums2[k]
                break

            # if all the elements of num2 has been placed in num1 
            elif j == n:
                break

            # if num1s element is greater than num2's 
            # place num2's element before num1's element
            elif nums1[i] > nums2[j]:
                nums1[i+1:] =  nums1[i:-1]
                nums1[i] = nums2[j]
                j += 1
                i += 1

            # if num1s element is smaller or equal to num2's element
            # go to next element in nums1
            else:
                i += 1