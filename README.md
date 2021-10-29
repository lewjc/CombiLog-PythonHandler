# CombiLog-PythonHandler

Python package containing custom log handler to integrate with CombiLog

## Installation

```
$ pip install combilog-handler
```

## Usage Guide

Example usage

```
import logging
from combilog_handler.loghandler import CombilogHandler

# Points to the Websocket Server Url hosted in the Combilog Aggregator.
url = "ws://AGG_DOMAIN:AGG_SOCKET_PORT"

# Secret of the service registered in the Combilog Dashboard
secret = "MY-SPECIAL-SECRET"

logger = logging.Logger("NamedService")
handler = CombilogHandler(aggregator_url=url, service_secret=secret)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

```
