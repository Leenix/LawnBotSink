from SinkNode.Formatter.CSVFormatter import *
from SinkNode.Reader.SerialReader import SerialReader
from SinkNode.Writer.LogFileWriter import LogFileWriter
from SinkNode import *
from SinkNode.Writer.ThingspeakWriter import ThingspeakWriter
from SinkNode.Writer.DweetWriter import DweetWriter


from lawbot_settings import LAWNBOT_KEY_MAP, log_format, logger_level


__author__ = 'Leenix'

logger = logging.getLogger("lawnbot")
sh = logging.StreamHandler()
lf = logging.Formatter(log_format)
sh.setFormatter(lf)
sh.setLevel(logger_level)
logger.addHandler(sh)

# Readers
reader = SerialReader("COM7", 115200,
                      start_delimiter='#',
                      stop_delimiter='$',
                      logger_level=logging.INFO)

# Loggers
file_logger = LogFileWriter(filename="lawnbot.log",
                            formatter=CSVFormatter(logger_level=logging.INFO),
                            logger_level=logging.DEBUG,
                            writer_id="CSVLog",
                            file_time_prefix="%Y-%m %B ")

# Writers
writer_lawnbot1 = ThingspeakWriter(writer_id="lawnbot1",
                                   api_key="CKQPCVOK2U31WOAT",
                                   key_map=LAWNBOT_KEY_MAP,
                                   logger_level=logging.INFO)

lawnbot_dweet = DweetWriter(writer_id="lawnbot1")


# Main
ingestor = SinkNode(reader, logger_level=logging.DEBUG)
ingestor.add_logger(file_logger)
ingestor.add_writer(writer_lawnbot1)
ingestor.add_writer(lawnbot_dweet)

ingestor.start()

try:
    while True:
        user_input = raw_input("Enter commands...")
        reader.ser.write(user_input)

except KeyboardInterrupt:
    ingestor.stop()
    print "woo woo woo woo"




