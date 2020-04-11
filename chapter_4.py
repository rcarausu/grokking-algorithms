"""
Divide & Conquer
It's a way of thinking about problems by reducing them to the base case,
 and then using recursion to solve them.

Quicksort
Consists in sorting choosing a D&C strategy based on an element called 'pivot'.
We separate the arrays, if it's the case, by comparing with this pivot and then we
call quicksort recursively on the sub arrays.
The pivot selection determines the execution time.
    Best case scenario, O(n*log n)
    Worst case scenario, O(n^2)

Average scenario by selecting a random pivot is O(n log n).
"""


# 4.1 Write out the code for he earlier sum function.
from random import randrange


def sum(items: []) -> int:
    if not items:
        return 0
    else:
        return items[0] + sum(items[1:])


# 4.2 Write a recursive function to count the number of items in a list.
def count_items(items: []) -> int:
    if not items:
        return 0
    else:
        return 1 + count_items(items[1:])


# 4.3 Find the maximum number in a list
def find_max(items: []) -> int:
    if len(items) == 1:
        return items[0]
    if not items:
        raise ValueError('list must contain at least one element')
    if len(items) == 2:
        return items[0] if items[0] > items[1] else items[1]
    sub_max = max(items[1:])
    return items[0] if items[0] > sub_max else sub_max


# 4.4 Can you come up with the base case and recursive case for binary search?
# Answer: base case is when the list has one element
# Recursive case is splitting the list in two halves, throwing away one and calling
# binary search on the remaining half


def quicksort(array: []) -> []:
    if len(array) < 2:
        return array
    pivot = array[randrange(len(array) - 1)]
    less = []
    greater = []
    for i in array:
        if i != pivot:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)

    return quicksort(less) + [pivot] + quicksort(greater)

# How long would each of these operations take in big O notation?
# 4.5 Printing the value of each element in an array
# A: O(n) because we iterate all values

# 4.6 Doubling the value of each element in an array
# A: This is to iterate all array O(n), and insert a new value, which is O(n) as well, so O(n)

# 4.7 Doubling the value of just the first element in an array.
# A: Search O(1) and insert O(n), so O(n)

# 4.8 Creating a multiplication table with all the elements in the array. So if your array i
# [2, 3, 7, 8, 10], you first multiply every element by 2, then multiply every element by 4,
# then by 7, and so on.
# A: We iterate all the array O(n), n times, so O(n^2).


if __name__ == '__main__':
    print(sum([2, 3, 1]))
    print(count_items([1, 2, 3]))
    print(find_max([1, 2, 27, 3, 4]))
    print(quicksort([23, 4, 1, 9, 29]))

