def swap(array: list, left: int, right: int):
    tmp: int = array[left]
    array[left] = array[right]
    array[right] = tmp


def swap_adjacent_numbers(array: list, i: int):
    swap(array, i - 1, i)
