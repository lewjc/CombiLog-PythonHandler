from logging import Handler, getLogger, Logger
from websocket import WebSocketApp, WebSocket, WebSocketConnectionClosedException
import json
import threading
import asyncio
import time
from queue import Queue
from combilog_handler.socketerror import get_closure_error


class CombilogHandler(Handler):
    def __init__(self, aggregator_url: str, service_secret: str, logger: Logger = None):
        Handler.__init__(self)
        self._aggregator_url = aggregator_url
        self._service_secret = service_secret
        self._message_queue = Queue()
        self._create_socket()
        self._socket_thread = self.__create_socket_thread()
        self._socket_thread.start()

    def _create_socket(self):
        self._websocket = WebSocketApp(
            self._aggregator_url + "?connectionType=service",
            header={"combilog-service-secret": self._service_secret},
            on_close=self._generate_on_close(),
            on_open=self._generate_on_open(),
            on_error=self._generate_on_error(),
        )

    def _connect(self):
        try:
            self._websocket.run_forever()
        except WebSocketConnectionClosedException as e:
            print(e)

    def __create_socket_thread(self):
        return threading.Thread(
            target=self._connect,            
            daemon=True,
        )

    def _generate_on_open(self):
        def on_open(ws: WebSocket):
            print("Combilog connection opened.")
            if not self._message_queue.empty():
                while not self._message_queue.empty():
                    ws.send(json.dumps(self._message_queue.get()))

        return on_open

    def _generate_on_close(self):
        def on_close(ws, code=0, reason=None):
            closure_reason = get_closure_error(code)
            print(
                "Combilog aggreagtor connection was closed. Reason: {} Attempting reconnect in 5 seconds...".format(
                    closure_reason
                )
            )
            threading.Timer(5, self._connect).start()

        return on_close

    def _generate_on_error(self):
        def on_error(ws: WebSocketApp, error: str):
            print("Combilog aggreagtor connection errored: " + error)
            threading.Timer(5, self._retry_connect).start()

        return on_error

    def emit(self, record):
        try:
            msg = self.format(record)
            message = {"type": 0, "content": msg}
            if self._websocket.sock != None and self._websocket.sock.connected:
                self._websocket.send(json.dumps(message))
            else:
                self._message_queue.put(message)

        except WebSocketConnectionClosedException as e:
            print(
                "Attempting to emit log from Combilog Handler failed. Check aggregator logs as connection was closed. Attempting reconnection"
            )
