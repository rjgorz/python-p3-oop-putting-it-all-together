#!/usr/bin/env python3

class Book:
    def __init__(self, title="Title", author="Author", page_count=0):
        self.title = title
        self.author = author
        self.page_count = page_count

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if isinstance(page_count, int) and page_count >= 0:
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")