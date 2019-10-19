"""
Binary Search
- It takes logarithmic time (or log time) guesses to find the answer.
Expressed as O(log n) in Big O notation.
"""

# Exercise 1.1
# log2 128 = 7

# Exercise 1.2
# log2 256 = 8

# Exercise 1.3
# O(log n), you can do it with binary search

# Exercise 1.4
# O(n)

# Exercise 1.5
# O(n)

# Exercise 1.6
# O(n), we do it until a certain limit but the time is still linear


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2  # // floor division
        guess = list[mid]

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
