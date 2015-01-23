import sys
from SinkNode.Processor.ThingspeakProcessor import ThingspeakProcessor
from SinkNode.Reader.SerialReader import SerialReader

__author__ = 'Leenix'

from SinkNode import *

from lawbot_settings import *

logger = logging.getLogger(logger_name)
logger.setLevel(logger_level)

# Console Logging
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(console_handler)

# File Logging
if log_filename:
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(logging.Formatter(log_format))
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

reader = SerialReader(port=SERIAL_PORT, baud_rate=SERIAL_BAUD, start_delimiter=PACKET_START, stop_delimiter=PACKET_STOP,
                      logger_name=logger_name)
processor = ThingspeakProcessor(key_map=LAWNBOT_KEY_MAP, channel_map=LAWNBOT_CHANNEL_MAP)
uploader = ThingspeakUploader(logger_name=None)

sink = SinkNode(reader, processor, uploader)
sink.run()


