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
