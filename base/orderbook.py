#!/usr/bin/python3


from base.defines import ASK, BID, DEFAULT_DEPTH, islice, pprint


class OrderBook(object):
    """거래소 베이스 클래스.
    """

    def __init__(self, pair, reverse=None):
        """Constructor.
        :param name: `str` 거래소 이름.
        :param pair: `str` 구독할 마켓 페어의 이름.
        :param asks: `dict` 매도호가 목록.
        :param bids: `dict` 매수호가 목록.
        :param book: `dict` 거래소 전체 정보 목록.
        """
        self.pair = pair
        self.name = self.get_name()
        self.asks = {}
        self.bids = {}
        self.book = self.create_frame()
        self.reverse = self._reverse
        
    
    def _reverse(self, side):
        """매도, 매수호가에 따른 내림차순, 오름차순 불린값 반환.
        """
        return False if side == ASK else True

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
        
    def remove(self, side, price):
        """오더북 특정 레벨의 주문을 삭제.
        """
        del self.book[side][price]
        
    def update(self, side, price, amount):
        """오더북 특정 레벨의 주문을 갱신.
        """
        self.book[side].update({price: amount})
        
    def insert(self, side, price, amount):
        """오더북 특정 주문을 삽입 후 정렬 및 슬라이싱.
        """
        self.book[side].update({price: amount})
        self.isorted(side)
        
    def sorted(self, frame, reverse):
        """오더북 아이템들을 정렬한다.
        """
        return sorted(frame.items(), reverse=reverse)
    
    def islice(self, frame, reverse, depths):
        """정렬된 딕셔너리를 슬라이싱한다.
        """
        return islice(self.sorted(frame, reverse), depths)
        
    def collect(self, frame, reverse, depths):
        return dict(self.islice(frame, reverse, depths))
    
    def isorted(self, side):
        self.book[side] = self.collect(frame=self.book[side],
                                       reverse=self.reverse(side),
                                       depths=DEFAULT_DEPTH)
        
    def bprint(self):
        """현재 거래소의 오더북을 pretty print로 출력하며,
        딕셔너리 정렬기능 기본값 False.
        """
        pprint(self.book, sort_dicts=False)