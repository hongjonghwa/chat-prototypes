import logging
from dotenv import load_dotenv

logging.basicConfig(
    # format='%(asctime)s - %(levelname)s - %(message)s',
    format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)

load_dotenv()
