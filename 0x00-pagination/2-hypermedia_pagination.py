#!/usr/bin/env python3
"""simple pagination
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
        """function that return a paginated data"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataIndex = self.index_range(page, page_size)
        self.dataset()
        return self.__dataset[dataIndex[0]:dataIndex[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """return the page in dict"""
        hyperRes = {}
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        next_page = page + 1 if page - 1 in range(1, total_pages) else None
        prev_page = page - 1 if page - 1 in range(1, total_pages) else None

        hyperRes['page_size'] = len(data)
        hyperRes['page'] = page
        hyperRes['data'] = data
        hyperRes['next_page'] = next_page
        hyperRes['prev_page'] = prev_page
        hyperRes['total_pages'] = total_pages

        return hyperRes

    def index_range(self, page, page_size):
        """function to do the above"""
        return ((page - 1) * page_size, page * page_size)
