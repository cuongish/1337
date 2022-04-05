from typing import List


def first_missing_positive(nums: List[int]) -> int:
    num_set = set(nums)
    for i in range(1, pow(2, 31) - 1):
        if i not in num_set:
            return i


A = [1, -1, 100, 3, 3, 6, 4, 7]
first_missing_positive(nums=A)
