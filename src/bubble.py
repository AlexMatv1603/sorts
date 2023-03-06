# Bubble sort algorithm - O(n^2)
from src.utils.swap import swap_adjacent_numbers


def bubble_sort(array: list):
    for j in range(len(array)):
        for i in range(len(array) - 1, j, -1):
            if (i != 0) and (array[i - 1] > array[i]):
                swap_adjacent_numbers(array, i)

