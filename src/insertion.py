# Insertion sort algorithm - O(n^2)
from src.utils.swap import swap_adjacent_numbers


def insertion_sort(array: list):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if (j != 0) and (array[j - 1] > array[j]):
                swap_adjacent_numbers(array, j)


arr = [8, 3, 5, 1, 6, 2, 4, 10, 7, 9]

insertion_sort(arr)
print(arr)
