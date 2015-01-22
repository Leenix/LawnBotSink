__author__ = 'Leenix'

from SinkNode import *

from lawbot_settings import *

logger = logging.basicConfig(level=logger_level)

sink = SinkNode(reader, processor, uploader)
sink.run()

