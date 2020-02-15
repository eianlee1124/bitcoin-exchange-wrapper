#!/usr/bin/python3


from lib.defines import ASK, BID, json
from lib.orderbook import OrderBook
from lib.websockets import WebSocketAPI
from lib.config import KrakenConfig as config


class Kraken(OrderBook):
    
    def __init__(self, pair, url, payload):
        super().__init__(pair)
        self.wss = WebSocketAPI()
        self.pair = pair
        self.url = url
        self.payload = payload
        
    def connect(self):
        self.wss.connect(self.url)
        
    def send(self):
        self.wss.send(json.dumps(self.payload))
        
    def snapshot(self, update):
        """크라켄 스냅샷이 수신되면 인-메모리에 저장할 프레임형태로
        포맷팅하여 반환.
        """
        snapshot = {}
        for price, amount, _ in update:
            snapshot[price] = amount
        return snapshot
    
    def process(self, side, price, amount):
        """크라켄 인-메모리 오더북 삽입, 갱신, 삭제 프로세스.
        """
        # 삭제
        if (float(amount) == 0 and price in self.book[side]):
            self.remove(side, price)
        # 갱신
        if (float(amount) == 0 and price in self.book[side]):
            self.update(side, price, amount)
        # 삽입
        if (float(amount) == 0 and price not in self.book[side]):
            self.insert(side, price, amount)
        
    def handler(self):
        """레벨3 오더북 메시지 핸들러.
        """
        message = json.loads(self.wss.recv())
        if not isinstance(message, list):
            return

        updates = message[1:-2]
        
        for update in updates:
            if 'as' in update:
                self.book[ASK] = self.snapshot(update['as'])
                self.book[BID] = self.snapshot(update['bs'])
            else:
                for s, order in update.items():
                    side = ASK if s == 'a' else BID
                    for price, amount, *_ in order:
                        self.process(side, price, amount)
                        
                        
if __name__ == "__main__":
    
    pair = "BTC/USD"
    url = config.url
    payload = config.payload
    payload['pair'] = [pair]
    
    kraken = Kraken(pair, url, payload)
    kraken.wss.connect(url)
    kraken.wss.send(payload)
    
    while True:
        kraken.handler()
        kraken.bprint()