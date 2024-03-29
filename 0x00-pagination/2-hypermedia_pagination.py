#!/usr/bin/env python3
"""Module"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end indices for a given page and page size.

    Args:
        page (int): The current page number (1-based index).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index (inclusive) and end index (exclusive).
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index

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
         """
        Retrieves the appropriate page of a dataset based on pagination parameters.

        Args:
        page (int, optional): The current page number (1-based index). Defaults to 1.
        page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
        list: The list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)

        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves hyperlinked pagination information for a dataset.

        Args:
        page (int, optional): The current page number (1-based index). Defaults to 1.
        page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
        dict: A dictionary containing pagination details.
        """

        current_page = get_page(page, page_size)

        total_items = len(current_page)
        total_pages = math.ceil(total_items / page_size)

        if page < total_pages:
            next_page = page + 1
        else:
            None
        if page > 1:
            prev_page = page - 1
        else:
            None

        pagination_info = {
        "page_size": len(current_page),
        "page": page,
        "data": current_page,
        "next_page": next_page,
        "prev_page": prev_page,
        "total_pages": total_pages
        }

        return pagination_info
