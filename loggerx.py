""" My Logger Xizuth
    """
import logging


class LogX:
    def __init__(self, name="", debug=False):
        self.name = f"= {name} ="
        self.debug = debug

        logging.basicConfig(
            filename="app.log",
            encoding="utf-8",
            filemode="a",
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(process)d",
            level=logging.DEBUG
        )

        self.log = logging.getLogger(name)

    def i(self, message):
        self.log.info(message)
        if self.debug:
            print(self.name, "Info:", message)

    def e(self, message, error=None):
        self.log.error(f"{message}, Track: {error}")
        if self.debug:
            print(self.name, "Error:", message, "Track:", error)

    def w(self, message):
        self.log.warning(message)
        if self.debug:
            print(self.name, "Warning:", message)

    def d(self, message):
        self.log.debug(message)
        if self.debug:
            print(self.name, "Debug:", message)
