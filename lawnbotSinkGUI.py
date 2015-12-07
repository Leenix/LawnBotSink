from Tkinter import *
from SinkNode.Processor.ThingspeakProcessor import ThingspeakProcessor
from SinkNode.Reader.SerialReader import SerialReader
from SinkNode import *
from lawbot_settings import *


class LawnbotSink(Frame):
    def __init__(self, serial=None):
        Frame.__init__(self)
        self.ser = serial
        self.master.title("Lawnbot Controller")
        self.grid()

        self.water_on_button = Button(self, text="Water On", command=self.water_on)
        self.water_on_button.grid(row=0, column=0)

        self.water_off_button = Button(self, text="Water Off")
        self.water_off_button.grid(row=0, column=1)

        self.request_sample_button = Button(self, text="Request sample")
        self.request_sample_button.grid(row=1, column=0, columnspan=2)

        self.increase_sample_period_button = Button(self, text="Increase sample period")
        self.increase_sample_period_button.grid(row=2, column=0)

        self.decrease_sample_period_button = Button(self, text="Decrease sample period")
        self.decrease_sample_period_button.grid(row=2, column=1)

        self.sensor_text = Text(self)
        self.sensor_text.grid(row=3, column=0, rowspan=2, columnspan=2)



    def water_on(self):
        ser.write("B$")

    def water_off(self):
        ser.write("b$")

    def request_sample(self):
        ser.write("r$")

    def increase_sample_period(self):
        ser.write("$")

    def decrease_sample_period(self):
        ser.write("$")


def start_logger():
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


def start_sink():
    pass


if __name__ == '__main__':
    start_logger()
    LawnbotSink().mainloop()

    reader = SerialReader(port=SERIAL_PORT, baud_rate=SERIAL_BAUD, start_delimiter=PACKET_START, stop_delimiter=PACKET_STOP,
                          logger_name=logger_name)
    processor = ThingspeakProcessor(key_map=LAWNBOT_KEY_MAP, channel_map=LAWNBOT_CHANNEL_MAP)
    uploader = ThingspeakUploader(logger_name=None)
    ser = reader.get_serial()

    sink = SinkNode(reader, processor, uploader)
    sink.start()
    LawnbotSink(ser).mainloop()