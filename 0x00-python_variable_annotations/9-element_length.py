#!/usr/bin/env python3
""" iterable object """


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ elemetn length function """
    return [(i, len(i)) for i in lst]
