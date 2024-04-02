#!/usr/bin/env python3
"""Module"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end indices for a given page and page size.

    Args:
        page (int): The current page number (1-based index).
        page_size (int): The number of items per page.

    Returns:
        tuple: 
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
         """
        Retrieves the appropriate page of a dataset
        based on pagination parameters.
        Args:
        page (int, optional): 
        page_size (int, optional): 
        Returns:
        list: 
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        index = index_range(page, page_size)

        start_index = index[[0]
        end_index = index[1]
        try:
            return self.dataset()[start_index:end_index]
        except IndexError:
            return []


