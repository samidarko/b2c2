# A b2c2 command line interface for the b2c2 api

The b2c2 cli is built on top of [click](https://click.palletsprojects.com/en/8.0.x/)

It uses the `b2c2_api` http client which is auto-generated from the swagger definition at the
root of this project `b2c2.yaml`

You'll find a script to generate the client named `generate_b2c2_api_python.sh`

The `b2c2_api` is located in "libs/python/b2c2_api"

Originally, I wanted to develop a React App as well but I already spent more than 2 hours doing the cli
but I left the axios based http client "libs/typescript/b2c2Api" in the repository and the 
associated script to generate it `generate_b2c2_api_typescript.sh`

## Use the mock server

```shell
$ python server.py
```

## how to use the project

Probably best to create a [virtualenv](https://docs.python.org/3/tutorial/venv.html) first

first install the library

```shell
$  pip install libs/python/b2c2_api 
```

then install the cli

```shell
$  pip install b2c2_cli
```

Finally, 

```shell
$  b2c2 --help

Usage: b2c2 [OPTIONS] COMMAND [ARGS]...

Options:
  --log-level TEXT
  --host TEXT
  --token TEXT
  --version         Show the version and exit.
  --help            Show this message and exit.

Commands:
  balances     Get Balances.
  instruments  List Instruments.
  order
  rfq          Send Request for Quotes.

```


## Examples

### Get balances

```shell
$ HOST=http://localhost:8000 TOKEN=123 b2c2 balances 
{'USD': '0', 'BTC': '0', 'JPY': '0', 'GBP': '0', 'ETH': '0', 'EUR': '0', 'CAD': '0', 'LTC': '0', 'XRP': '0', 'BCH': '0'}
```

### Get instruments

```shell
$ HOST=http://localhost:8000 TOKEN=123 b2c2 instruments 
[{'name': 'BTCUSD.CFD'}, {'name': 'BTCUSD.SPOT'}, {'name': 'BTCEUR.SPOT'}, {'name': 'BTCGBP.SPOT'}, {'name': 'ETHBTC.SPOT'}, {'name': 'ETHUSD.SPOT'}, {'name': 'LTCUSD.SPOT'}, {'name': 'XRPUSD.SPOT'}, {'name': 'BCHUSD.SPOT'}]
```

### Pass an order

```shell
$ HOST=http://localhost:8000 TOKEN=123 b2c2 order BTCUSD.SPOT buy 1 7505161e-0181-4149-9877-7e737eddef52 700 FOK 2018-02-06T16:07:50.122206Z risk-adding-strategy 
{'client_order_id': 'd4e41399-e7a1-4576-9b46-349420040e1a',
 'created': '2018-02-06T16:07:50.122206Z',
 'executed_price': '10457.651100000',
 'executing_unit': 'risk-adding-strategy',
 'instrument': 'BTCUSD.SPOT',
 'order_id': 'd4e41399-e7a1-4576-9b46-349420040e1a',
 'price': '11000.00000000',
 'quantity': '3.0000000000',
 'side': 'buy',
 'trades': [{'created': '2018-02-26T14:27:53.675962Z',
             'executing_unit': 'risk-adding-strategy',
             'instrument': 'BTCUSD.SPOT',
             'order': 'd4e41399-e7a1-4576-9b46-349420040e1a',
             'origin': 'rest',
             'price': '10457.65110000',
             'quantity': '3.0000000000',
             'side': 'buy',
             'trade_id': 'b2c50b72-92d4-499f-b0a3-dee6b37378be'}]}
```

### Request For Quote

```shell
$ HOST=http://localhost:8000 TOKEN=123 b2c2 rfq BTCUSD.SPOT buy 1 7505161e-0181-4149-9877-7e737eddef52
your quote:
{'client_rfq_id': '149dc3e7-4e30-4e1a-bb9c-9c30bd8f5ec7',
 'created': '2018-02-06T16:07:50.122206Z',
 'instrument': 'BTCUSD.SPOT',
 'price': '700.00000000',
 'quantity': '1.0000000000',
 'rfq_id': 'd4e41399-e7a1-4576-9b46-349420040e1a',
 'side': 'buy',
 'valid_until': '2017-01-01T19:45:22.025464Z'}
do you want to pass this order? [y/n]: y
{'client_order_id': 'd4e41399-e7a1-4576-9b46-349420040e1a',
 'created': '2018-02-06T16:07:50.122206Z',
 'executed_price': '10457.651100000',
 'executing_unit': 'risk-adding-strategy',
 'instrument': 'BTCUSD.SPOT',
 'order_id': 'd4e41399-e7a1-4576-9b46-349420040e1a',
 'price': '11000.00000000',
 'quantity': '3.0000000000',
 'side': 'buy',
 'trades': [{'created': '2018-02-26T14:27:53.675962Z',
             'executing_unit': 'risk-adding-strategy',
             'instrument': 'BTCUSD.SPOT',
             'order': 'd4e41399-e7a1-4576-9b46-349420040e1a',
             'origin': 'rest',
             'price': '10457.65110000',
             'quantity': '3.0000000000',
             'side': 'buy',
             'trade_id': 'b2c50b72-92d4-499f-b0a3-dee6b37378be'}]}

```