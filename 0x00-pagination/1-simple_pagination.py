#!/usr/bin/env python3
"""1-0-simple_helper_function module"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Finds the correct indexes to paginate dataset.
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        file_size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, file_size)
        if start >= file_size:
            return []
        return self.dataset()[start:end]


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
