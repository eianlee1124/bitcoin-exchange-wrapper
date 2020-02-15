#!/usr/bin/python3


class OrderBook(object):
    """오더북 베이스 클래스.
    """
    
    def __init__(self, pair):
        self.name = self.get_name()
        self.pair = pair
        self.asks = {}
        self.bids = {}
        self.book = self.create_frame()