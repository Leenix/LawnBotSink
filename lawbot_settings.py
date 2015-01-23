__author__ = 'Leenix'

from SinkNode.Uploader.ThingspeakUploader import *

logger_level = logging.INFO
logger_name = "lawnbot"
log_filename = "lawnbot.log"
log_format = "%(asctime)s - %(levelname)s - %(message)s"

# Reader Settings #########################################

SERIAL_PORT = "COM4"
SERIAL_BAUD = 57600

PACKET_START = '#'
PACKET_STOP = '$'


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
    "lawnbot1": "API KEY",
    "lurker1": "<API_KEY>"
}



# Uploader Settings #######################################



