# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
from typing import List


def list_of_multiples_of_3_or_5(ar: List[str]) -> List[str]:
    multiples = [i for i in ar if i % 3 == 0 or i % 5 == 0]
    return multiples


sum(list_of_multiples_of_3_or_5(list(range(1000))))  # 233168
