# Selection sort algorithm - O(n^2)
from src.utils.swap import swap


def selection_sort(array: list):
    for i in range(len(array)):
        min_val_index = i
        for j in range(i, len(array)):
            if array[min_val_index] > array[j]:
                min_val_index = j

        if min_val_index != i:
            swap(array, i, min_val_index)

