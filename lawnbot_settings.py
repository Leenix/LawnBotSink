import logging

__author__ = 'Leenix'

logger_level = logging.INFO
logger_name = "lawnbot"
log_filename = "lawnbot.log"
log_format = "%(asctime)s - %(levelname)s - %(message)s"

# Reader Settings #########################################

SERIAL_PORT = "/dev/ttyUSB0"
SERIAL_BAUD = 115200

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
    "lawnbot1": "CKQPCVOK2U31WOAT",
    "lurker1": "CKQPCVOK2U31WOAT"
}



# Uploader Settings #######################################



