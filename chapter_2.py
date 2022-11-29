"""
2. SELECTION SORT

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


def find_smallest_index(arr: []) -> int:
    if len(arr) > 0:
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index
    return None


def selection_sort(arr: []) -> []:
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
