#!/usr/bin/env python3
"""anotate a list"""


def sum_list(input_list: list[int]) -> float:
    """the function """

    y: float = 0
    for x in range(len(input_list)):
        y += input_list[x]
    return y
