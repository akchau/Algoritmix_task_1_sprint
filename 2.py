"""id = 72129867"""
from collections import Counter
from typing import List, Tuple


def get_uniq_arr(arr):
    unique_arr = []
    for element in arr:
        if element in unique_arr:
            continue
        unique_arr.append(element)
    return unique_arr


def count_point(n, arr):
    unique_arr = get_uniq_arr(arr)
    summ_point = 0
    c = Counter(arr)
    for element_of_unique_arr in unique_arr:
        if c[element_of_unique_arr] <= n*2:
            summ_point += 1
    return summ_point


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    final_massive = ''
    for i in range(4):
        final_massive += input().replace('.', '')
    arr = list(map(int, final_massive))
    return n, arr


if __name__ == "__main__":
    n, arr = read_input()
    print(count_point(n, arr))
