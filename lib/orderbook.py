#!/usr/bin/python3


class OrderBook(object):
    """오더북 베이스 클래스.
    """

    def __init__(self, pair):
        """Constructor.
        :param name: `str` 거래소 이름.
        :param pair: `str` 구독할 마켓 페어의 이름.
        :param asks: `dict` 매도호가 목록.
        :param bids: `dict` 매수호가 목록.
        :param book: `dict` 거래소 전체 정보 목록.
        """
        self.name = self.get_name()
        self.pair = pair
        self.asks = {}
        self.bids = {}
        self.book = self.create_frame()

    def get_name(self):
        """거래소 클래스의 이름을 반환.
        """
        return self.__class__.__name__
    
    def create_frame(self):
        """거래소 전체 정보가 담긴 프레임을 반환.
        """
        return dict(name=self.name,
                    pair=self.pair,
                    asks=self.asks,
                    bids=self.bids)