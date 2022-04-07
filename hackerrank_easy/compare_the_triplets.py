#!/bin/python3

import os
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compare_triplets(a, b):
    # Write your code here
    sum_a = 0
    sum_b = 0
    for x, y in zip(a, b):
        if x > y:
            sum_a += 1
        if y > x:
            sum_b += 1
    return sum_a, sum_b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compare_triplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
