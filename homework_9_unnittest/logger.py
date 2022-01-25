import logging
import sys
import os

log = logging.getLogger("MYFIRSTLOGGERFORHOMEWORK")
log.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
log.addHandler(stream_handler)
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'apply.log')
file_handler = logging.FileHandler(filename, encoding= "utf8")
log.addHandler(file_handler)



