""" My Logger - Xizuth

Example:

log = LogX(__name__, level=logging.DEBUG)

log.i("information",...)
log.e("e", e.message)
log.w("warning", )
log.i("information", msg)
log.d("Debug", msg)
    """

import logging


class LogX:
    def __init__(self, name="", debug=False, level=logging.DEBUG):

        self.name = f"= {name} ="
        self.debug = debug

        logging.basicConfig(
            filename="app.log",
            encoding="utf-8",
            filemode="a",
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(process)d",
            level=level,
        )

        self.log = logging.getLogger(name)

    def i(self, message, *args):

        for m in args:
            message += "\n" + m

        message = f"{self.name} - Info: {message}"

        if self.debug:
            print(message)
        self.log.info(message)
        return message

    def e(self, message, error="", *args):

        for m in args:
            message += "\n" + m

        message = f"{self.name} - Error: {message}, Track: {error}"

        if self.debug:
            print(message)

        self.log.error(f"{message}, Track: {error}")

        return message

    def w(self, message, *args):
        for m in args:
            message += "\n" + m

        message = f"{self.name} - Warning: {message}"

        if self.debug:
            print(message)
        self.log.warning(message)

    def d(self, message, *args):
        for m in args:
            message += "\n" + m

        message = f"{self.name} - Debug: {message}"

        if self.debug:
            print(message)
        self.log.debug(message)
        return message
