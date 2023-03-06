# Bubble sort algorithm
from src.utils.swap import swap_adjacent_numbers


def bubble_sort(array: list):
    for j in range(len(array)):
        for i in range(len(array) - 1 - j, -1, -1):
            if i != len(array) - 1:
                swap_adjacent_numbers(array, i)


arr = [8, 3, 5, 1, 2, 4, 10, 7, 9]

bubble_sort(arr)
