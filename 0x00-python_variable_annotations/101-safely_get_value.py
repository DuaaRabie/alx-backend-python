#!/usr/bin/env python3
""" More involved type annotations """


from typing import Mapping, Any, TypeVar, Optional, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None)\
        -> Union[Any, T]:
    """ safely get value """
    if key in dct:
        return dct[key]
    else:
        return default
