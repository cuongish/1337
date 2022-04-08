if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    new_sorted_list = sorted(set(arr))

    print(new_sorted_list[-2])
