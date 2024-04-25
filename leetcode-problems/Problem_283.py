from typing import List


# WHAT I DID
# def moveZeroes(nums: List[int]) -> None:
#     count = 0
#     i = 0
#
#     while i < len(nums):
#         if nums[i] == 0:
#             count += 1
#             nums.remove(0)
#         else:
#             i += 1
#
#     nums.extend([0] * count)

# BETTER WAY - TWO POINTER APPROACH

def moveZeroes(self, nums: List[int]) -> List:
    left = 0
    for right in range(len(nums)):
        if nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums
