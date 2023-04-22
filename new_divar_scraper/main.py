"""Main"""
import os

from .divar.scraper import fetch_url_data

while True:
    url = os.getenv("URL")
    fetch_url_data(url)
    break
