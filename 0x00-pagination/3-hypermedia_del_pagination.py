#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves hyperlinked pagination information for a dataset based on index.

        Args:
        index (int, optional): The current start index (0-based). Defaults to None.
        page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
        dict: A dictionary containing pagination details.
        """
        assert isinstance(index, int) and index > 0

        if index is None:
            current_index = 0
        else:
            current_index = index

        next_index = current_index + page_size
        current_page = dataset[current_index:next_index]

        pagination_info = {
        "index": current_index,
        "next_index": next_index,
        "page_size": page_size,
        "data": current_page
        }

        return pagination_info
