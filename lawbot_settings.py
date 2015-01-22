__author__ = 'Leenix'

from SinkNode.Reader.SerialReader import *
from SinkNode.Processor.ThingspeakProcessor import *
from SinkNode.Uploader.ThingspeakUploader import *

logger_level = logging.INFO

# Reader Settings #########################################

SERIAL_PORT = "COM4"
SERIAL_BAUD = 57600

PACKET_START = '#'
PACKET_STOP = '$'

reader = SerialReader(port=SERIAL_PORT, baud_rate=SERIAL_BAUD, start_delimiter=PACKET_START, stop_delimiter=PACKET_STOP)


# Processor Settings ######################################

LAWNBOT_KEY_MAP = {
    "temperature": "field1",
    "humidity": "field2",
    "illuminance": "field3",
    "soil_moisture": "field4",
    "water_flow": "field5",
    "soil_temp": "field6",
    "soil_humd": "field7",
}

LAWNBOT_CHANNEL_MAP = {
    "lawnbot1": "API KEY"
}

processor = ThingspeakProcessor(key_map=LAWNBOT_KEY_MAP, channel_map=LAWNBOT_CHANNEL_MAP)


# Uploader Settings #######################################

uploader = ThingspeakUploader()

