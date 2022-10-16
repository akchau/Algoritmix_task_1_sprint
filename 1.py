"""id = 72255102"""
from typing import List, Tuple


def length_to_zero(n, arr):

    def full_before_first_zero_index():
        g = 1
        for reverse_index in range(first_zero_index-1, -1, -1):
            length_to_zero[reverse_index] = g
            g += 1
        return length_to_zero

    def full_after_last_zero_index():
        g = 1
        for direct_index in range(last_zero_index+1, len(length_to_zero),):
            length_to_zero[direct_index] = g
            g += 1
        return length_to_zero

    zero_arr = []
    for index, value in enumerate(arr):
        if not value:
            zero_arr.append(index)
    first_zero_index = zero_arr[0]
    last_zero_index = zero_arr[-1]
    length_to_zero = [0]*n
    length_to_zero = full_before_first_zero_index()
    length_to_zero = full_after_last_zero_index()
    left_index = zero_arr[0] + 1
    right_cnt = 0
    while left_index < last_zero_index:
        right_cnt += 1
        right_index = zero_arr[right_cnt] - 1
        step = 1
        while right_index >= left_index:
            length_to_zero[right_index] = step
            length_to_zero[left_index] = step
            left_index += 1
            right_index -= 1
            step += 1
        left_index = zero_arr[right_cnt] + 1
    return length_to_zero


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    return n, arr


if __name__ == "__main__":
    n, arr = read_input()
    result = length_to_zero(n, arr)
    print(*result)
