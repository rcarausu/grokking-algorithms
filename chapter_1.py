"""
1. INTRODUCTION TO ALGORITHMS

Binary Search
- It takes logarithmic time (or log time) guesses to find the answer.
Expressed as O(log n) in Big O notation.

It requires a sorted list o perform the search.
"""
from typing import List


def binary_search(sorted_list: List, item: int) -> int:
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2  # // floor division
        guess = sorted_list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 13]
    print(binary_search(my_list, 3))
