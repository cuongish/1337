# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci
# sequence whose values do not exceed four million, find the sum of the even-valued terms.


def filter_even_fib_numbers_under_4mil():
    k, k1 = 1, 2
    sum = 0
    while k1 < 4000000:
        k2 = k+k1
        k, k1 = k1, k2
        if k2 % 2 == 0:
            sum += k2
    return sum


total = filter_even_fib_numbers_under_4mil()
print(total)  # 4613730
