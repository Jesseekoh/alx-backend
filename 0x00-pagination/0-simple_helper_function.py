#!/usr/bin/env python3
"""index_range module"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple containing a start index and an end
    index corresponding to the parameters

    Args:
        page (int): start index
        page_size (int): end index

    Returns:
        tuple:
    """
    start_idx = (page_size * page) - page_size
    end_idx = page_size * page
    return (start_idx, end_idx)
