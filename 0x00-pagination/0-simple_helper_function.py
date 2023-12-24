#!/usr/bin/env python3
"""
This module consists of a function named index_range that takes two
integer arguments page and page_size return a tuple
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns a tuple of start and end indexes for pagination.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: Start and end indexes for the requested page.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
