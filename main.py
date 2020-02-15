


def main(exchange, pair, url, payload):
    ex = exchange(pair, url, payload)
    ex.connect()
    ex.send()
    
    while True:
        ex.handler()
        ex.bprint()
        
        
if __name__ == "__main__":
    from base.config import KrakenConfig as config
    from exchange.kraken import Kraken
    
    pair = "BTC/USD"
    url = config.url
    payload = config.payload
    payload['pair'] = [pair]
    
    main(Kraken, pair, url, payload)
    