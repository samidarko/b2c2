import logging
import http.server
import json
import socketserver
import sys

PORT = 8000

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        logger.info(f"[GET] {self.path}")
        self.send_response_only(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        payload = {}
        if self.path == '/balance':
            payload = {
                "USD": "0",
                "BTC": "0",
                "JPY": "0",
                "GBP": "0",
                "ETH": "0",
                "EUR": "0",
                "CAD": "0",
                "LTC": "0",
                "XRP": "0",
                "BCH": "0"
            }
        if self.path == "/instruments":
            payload = [
                {
                    "name": "BTCUSD.CFD"
                },
                {
                    "name": "BTCUSD.SPOT"
                },
                {
                    "name": "BTCEUR.SPOT"
                },
                {
                    "name": "BTCGBP.SPOT"
                },
                {
                    "name": "ETHBTC.SPOT"
                },
                {
                    "name": "ETHUSD.SPOT"
                },
                {
                    "name": "LTCUSD.SPOT"
                },
                {
                    "name": "XRPUSD.SPOT"
                },
                {
                    "name": "BCHUSD.SPOT"
                }
            ]
        self.wfile.write(json.dumps(payload).encode())

    def do_POST(self) -> None:
        logger.info(f"[POST] {self.path}")
        self.send_response_only(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        payload = {}
        if self.path == "/request_for_quote":
            payload = {
                "valid_until": "2017-01-01T19:45:22.025464Z",
                "rfq_id": "d4e41399-e7a1-4576-9b46-349420040e1a",
                "client_rfq_id": "149dc3e7-4e30-4e1a-bb9c-9c30bd8f5ec7",
                "quantity": "1.0000000000",
                "side": "buy",
                "instrument": "BTCUSD.SPOT",
                "price": "700.00000000",
                "created": "2018-02-06T16:07:50.122206Z"
            }
        if self.path == "/order":
            payload = {
                "order_id": "d4e41399-e7a1-4576-9b46-349420040e1a",
                "client_order_id": "d4e41399-e7a1-4576-9b46-349420040e1a",
                "quantity": "3.0000000000",
                "side": "buy",
                "instrument": "BTCUSD.SPOT",
                "price": "11000.00000000",
                "executed_price": "10457.651100000",
                "executing_unit": "risk-adding-strategy",
                "trades": [
                    {
                        "instrument": "BTCUSD.SPOT",
                        "trade_id": "b2c50b72-92d4-499f-b0a3-dee6b37378be",
                        "origin": "rest",
                        "rfq_id": None,
                        "created": "2018-02-26T14:27:53.675962Z",
                        "price": "10457.65110000",
                        "quantity": "3.0000000000",
                        "order": "d4e41399-e7a1-4576-9b46-349420040e1a",
                        "side": "buy",
                        "executing_unit": "risk-adding-strategy"
                    }
                ],
                "created": "2018-02-06T16:07:50.122206Z"
            }
        self.wfile.write(json.dumps(payload).encode())


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    logger.info(f"serving at port {PORT}")
    httpd.serve_forever()
