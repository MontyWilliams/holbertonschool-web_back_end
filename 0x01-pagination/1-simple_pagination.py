#!/usr/bin/env python3
""" this actually performs the pagination
"""

import csv
import math
from typing import List

def index_range(page: int, page_size: int) -> tuple:
    """Get start and ending position
    """
    start = ((page - 1) * page_size)
    end = (start + page_size)
    result = (start, end)

    return result

class Server:
  """ Server class to paginate a database of popular baby names
  """
  DATA_FILE = "Popular_Baby_Names.csv"

  def __init__(self):
    self.__dataset = None

  def dataset(self) -> List[List]:
    """ Cached dataset 
    """
    if self.__dataset is None:
      with open(self.DATA_FILE) as f:
        reader = csv.reader(f)
        dataset = [row for row in reader]
      self.__dataset = dataset[1:]

    return self.__dataset

  def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """ verify arguments type as in and use
        index_range func to find correct indexes
        if args are out of range return empty list
    """
    assert type(page) == int and page > 0
    assert type(page_size) == int and page_size > 0
    start, end = index_range(page, page_size)
    pages = []
    if start >= len(self.dataset()):
        return pages
    pages = self.dataset()
    return pages[start:end]