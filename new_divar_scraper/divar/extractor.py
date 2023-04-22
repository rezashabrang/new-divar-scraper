from hashlib import sha1


def build_href(href: str):
    """Build full href from partial one."""
    return f"http://divar.ir{href}"


def create_id(full_href: str):
    """create id hash from full href."""
    return sha1(full_href.encode()).hexdigest()


def extract_rent_price(rent_text: str):
    return rent_text.replace("اجاره: ", "").replace(" تومان", "")


def extract_deposit_price(deposit_text: str):
    return deposit_text.replace("ودیعه: ", "").replace(" تومان", "")


def extract_region(region_name: str):
    return region_name.split(" در ")[1]
