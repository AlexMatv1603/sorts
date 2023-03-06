def swap_adjacent_numbers(array: list, i: int):
    if array[i] > array[i + 1]:
        tmp: int = array[i + 1]
        array[i + 1] = array[i]
        array[i] = tmp
