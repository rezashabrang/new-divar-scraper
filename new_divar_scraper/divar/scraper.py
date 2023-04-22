import requests
from bs4 import BeautifulSoup

from .extractor import (
    build_href,
    create_id,
    extract_deposit_price,
    extract_region,
    extract_rent_price,
)


def fetch_url_data(url):
    """Fetch the url data"""
    req = requests.get(url)
    page_data = req.content
    htmls = BeautifulSoup(page_data, "html.parser")
    items = htmls.select(".post-card-item-af972")

    items_metadata = []
    for item in items:
        href = build_href(item.find_all("a")[0].get("href"))

        item_meta = {
            "id": create_id(href),
            "href": href,
            "title": item.find_all("a")[0].get("title"),
            "deposit": extract_deposit_price(
                item.select(".kt-post-card__description")[0].text
            ),
            "rent": extract_rent_price(
                item.select(".kt-post-card__description")[1].text
            ),
            "region": extract_region(
                item.select(".kt-post-card__bottom-description")[0].text
            ),
        }

        items_metadata.append(item_meta)

        break
