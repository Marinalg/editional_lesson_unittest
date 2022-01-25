import logging
import sys

log = logging.getLogger("MYFIRSTLOGGERFORHOMEWORK")
log.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
log.addHandler(stream_handler)



