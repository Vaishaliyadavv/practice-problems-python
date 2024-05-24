from typing import List


def removeElement(self, nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


print(removeElement([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
