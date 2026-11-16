import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

logging.info(datetime.now().strftime("%Y-%m-%d"))
