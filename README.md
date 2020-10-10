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
import combilog_handler

# Points to the Websocket Server Url hosted in the Combilog Aggregator.
url = "ws://localhost:1337"

# Secret of the service registered in the Combilog Dashboard
secret = "MY-SPECIAL-SECRET"

logger = logging.Logger("NamedService")
handler = combilog_handler.loghandler.CombilogHandler(url, secret)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

```
