#!/usr/bin/python3


from defines import WebSocket, sslopt


class WebSocketAPI(object):
    
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