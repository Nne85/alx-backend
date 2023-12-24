#!/usr/bin/env python3
"""
a method named get_page that takes two integer arguments page
with default value 1 and page_size with default value 10.
"""

import csv
import math
from typing import List, Tuple


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Paginate parameters"""
        assert isinstance(page, int) and page > 0, "Page must be a positive\
        integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size\
        must be a positive integer."

        start_idx, end_idx = Server.index_range(page, page_size)
        dataset = self.dataset()

        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]
