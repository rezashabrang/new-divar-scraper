"""Main"""
import os

from .db import filter_new_items, initialize_mysql
from .divar.scraper import fetch_url_data
from .logger import LOGGER
from .notif.telegram import send_item as telegram
from .tools import zzz

LOGGER.info(f"Starting divar scraper for project '{os.getenv('PROJECT_NAME')}'.")

LOGGER.info("Initialzing database.")
initialize_mysql(os.getenv("PROJECT_NAME"))


LOGGER.info("Starting main loop.")
while True:
    url = os.getenv("URL")
    LOGGER.info("Fetching items from divar.")
    items_data = fetch_url_data(url)

    LOGGER.info("Filtering new items.")
    new_items = filter_new_items(items_data)

    # Send notification for new ones on Gmail and Telegram
    LOGGER.info("Sending new items.")
    for item in new_items:
        telegram(item)
    # TODO Gmail notification function

    # Sleep
    zzz()
