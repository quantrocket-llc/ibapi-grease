# ibapi-grease
The official Interactive Brokers Python API has a few warts which make it run slowly. Specifically: excessive debug logging, and an overly cautious lock on the socket connection. `ibapi-grease` provides monkey patches to eliminate these bottlenecks.

As an example of the speedup, making a socket connection to TWS goes from taking a second or more without `ibapi-grease` to a few milliseconds with it.

Without:

```python
In [1]: from ibapi.client import EClient

In [2]: from ibapi.wrapper import EWrapper

In [3]: class App(EWrapper, EClient):
   ...:     
   ...:      def __init__(self):
   ...:          EWrapper.__init__(self)
   ...:          EClient.__init__(self, wrapper=self)
   ...:         

In [4]: app = App()

In [5]: %time app.connect("localhost", 4001, 1)
CPU times: user 3.74 ms, sys: 2.44 ms, total: 6.17 ms
Wall time: 1.03 s

```

With:

```python
In [1]: from ibapi.client import EClient

In [2]: from ibapi.wrapper import EWrapper

In [3]: from ibapi_grease import patch_all

In [4]: patch_all()

In [5]: class App(EWrapper, EClient):
   ...:     
   ...:      def __init__(self):
   ...:          EWrapper.__init__(self)
   ...:          EClient.__init__(self, wrapper=self)
   ...:         

In [6]: app = App()

In [7]: %time app.connect("localhost", 4001, 1)
CPU times: user 3.83 ms, sys: 1.72 ms, total: 5.55 ms
Wall time: 13.9 ms
```

## Installation


```
pip install ibapi-grease
```

## Usage

```python
from ibapi_grease import patch_all
patch_all()
```

## Requirements

Naturally, `ibapi-grease` requires the [Interactive Brokers Python API](https://interactivebrokers.github.io/).

## License

`ibapi-grease` is distributed under the Apache 2.0 License. See the LICENSE file in the release for details.

## Note

`ibapi-grease` is not a product of Interactive Brokers, nor is this project affiliated with IB.



