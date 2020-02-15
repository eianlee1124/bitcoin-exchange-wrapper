#!/usr/bin/python3


"""
웹소켓 연결을 위한 베이스 클래스.
현재 최소한의 연결을 위한 메서드만 구현 되어 있음.
"""


from lib.defines import sslopt
from lib.defines import WebSocket
from lib.orderbook import OrderBook



class WebSocketAPI(object):
    """웹소켓 베이스 클래스.
    """
    
    def __init__(self):
        """Constructor.
        :param ws: `object` 웹소켓 모듈 객체.
        :param connect: 웹소켓 연결.
        :param send: 웹소켓 페이로드 전송.
        :param recv: 웹소켓 바이트 데이터 수신.
        :param close: 웹소켓 연결 종료.
        :param connected: 웹소켓 연결 상태.
        """
        self.ws = WebSocket(sslopt=sslopt)
        self.connect = self.ws.connect
        self.send = self.ws.send
        self.recv = self.ws.recv
        self.close = self.ws.close
        self.connected = self.ws.connected