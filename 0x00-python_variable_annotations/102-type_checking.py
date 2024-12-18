#!/usr/bin/env python3
""" Type checking """


from typing import List, Tuple, cast, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in the array by repeating each element a specified number of times.
    Args:
    lst (Tuple): The input list to be zoomed.
    factor (Union[int, float]): The factor by which to zoom in. Defaults to 2.
    Returns:
    Tuple: A new tuple containing the zoomed elements.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), 3)
