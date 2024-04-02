#!/usr/bin/env python3
"""Module"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end indices page and page size.
    Args:
        page (int): The current page number (1-based index).
        page_size (int): The number of items per page.
    Returns:
        tuple:
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
