"""
Sorting
- Arrays: items stored consecutively in memory.
    Easy to navigate randomly between them with simple arithmetic.
    Have to reserve memory for all the items.
    Reading is O(1), Insertion is O(n).
- Linked lists: each item stores the position of the next.
     Don't have to store items consecutively.
     Need to start from the first items to find an item since can't go backwards easily.
     Reading is O(n), Insertion is O(1).

- Selection sort
Search all elements O(n) and copy the items in a new list O(n).
Total cost of the operation is O(n^2)
"""


# Exercise 2.1
# Better to use a list, since there are few reads and many inserts,
# and we read the whole list only once at the end of the month.

# Exercise 2.2
# Better a list, since we mostly insert and delete items from it.

# Exercise 2.3
# As an array, since reading is O(1), otherwise the search would be O(n)

# Exercise 2.4
# The downsides for an array for inserts is that you need to calculate if you have enough memory each time,
# if not, we need to copy the whole chunk into a new data structure.
# If we use binary search for logins and we add new users to the array, it can happen that the search
# is not performed correctly.

# Exercise 2.5
# Searching is slower than arrays, but faster than linked lists since we divide by letters of the alphabet.
# Insertion is faster than arrays, since the size of the array is fixed and we don't deal with that, and more
# or less the same compared with linked lists


def find_smallest_index(arr: list):
    if len(arr) > 0:
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index
    return None


def selection_sort(arr: list):
    new_array = []

    for i in range(0, len(arr)):
        smallest_index = find_smallest_index(arr)
        new_array.append(arr[smallest_index])
        arr.pop(smallest_index)
    return new_array


if __name__ == "__main__":
    array = [23, 5, 12, 6, 8, 34, 2, 6, 34, 235]
    print(array)
    sorted_array = selection_sort(array)
    print(sorted_array)
