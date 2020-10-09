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
import combilog.loghandler

# Points to the Websocket Server Url hosted in the Combilog Aggregator.
url = "ws://localhost:1337"

# Secret of the service registered in the Combilog Dashboard
secret = "MY-SPECIAL-SECRET"

logger = logging.Logger("NamedService")
combilog_handler = combilog.loghandler.CombilogHandler(url, secret)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
combilog_handler.setFormatter(formatter)
logger.addHandler(combilog_handler)

```
