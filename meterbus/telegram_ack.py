from .exceptions import MBusFrameDecodeError, MBusFrameCRCError, FrameMismatch


class TelegramACK(object):
    @staticmethod
    def parse(data):
        if data is not None and len(data) < 1:
            raise MBusFrameDecodeError("Invalid M-Bus length")

        if data[0] != 0xE5:
            raise FrameMismatch()

        return TelegramACK()

    def __init__(self, dbuf=None):
        self.type = 0xE5
        self.base_size = 1
