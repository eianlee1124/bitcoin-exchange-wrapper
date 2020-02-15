


def main():
    from lib.exchange.kraken import Kraken, config
    pair = "BTC/USD"
    url = config.url
    payload = config.payload
    payload['pair'] = [pair]

    kraken = Kraken(pair, url, payload)
    kraken.wss.connect(url)
    kraken.wss.send()
    
    while True:
        kraken.handler()
        kraken.bprint()