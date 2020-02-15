#!/usr/bin/python3


import ssl
import base64
import hashlib
import hmac
import time
import itertools
import httplib2
import simplejson as json
import websocket



ASK = "asks"
BID = "bids"
DEFAULT_DEPTH = 10

islice = itertools.islice
WebSocket = websocket.WebSocket
sslopt = {"cert_reqs": ssl.CERT_NONE}
    