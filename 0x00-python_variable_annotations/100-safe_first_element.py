#!/usr/bin/env python3
""" first element of sequence """


from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ safe first element """
    if lst:
        return lst[0]
    else:
        return None