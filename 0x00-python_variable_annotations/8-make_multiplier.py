#!/usr/bin/env python3
""" complex types - functions """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multipling function """
    return lambda x: x * multiplier
