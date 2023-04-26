import os

from telethon import TelegramClient, sync

from ..logger import LOGGER

TEL_API_ID = int(os.getenv("TEL_API_ID"))
TEL_API_HASH = os.getenv("TEL_API_HASH")
TEL_BOT_TOKEN = os.getenv("TEL_BOT_TOKEN")
ASM_PROXY_ADDRESS = os.getenv("ASM_PROXY_ADDRESS")
ASM_PROXY_PORT = int(os.getenv("ASM_PROXY_PORT"))
USERNAME = os.getenv("USERNAME")


def construct_message(metadata):
    """Construct message from metadata!"""
    return f"""
\U0001F3E0 title: {metadata['title']}
\U0001F4B0 deposit: {metadata['deposit']}
\U0001F4B8 rent: {metadata['rent']}
\U0001F4CD region: {metadata['region']}

\U0001F517 {metadata['href']}
    """


def send_item(item_data):
    try:
        # Constructing message
        msg = construct_message(item_data)

        # Intantiating Telegram Client
        client = TelegramClient(
            "health_messenger",
            TEL_API_ID,
            TEL_API_HASH,
            proxy=(
                "socks5",
                ASM_PROXY_ADDRESS,
                ASM_PROXY_PORT,
            ),
        ).start(bot_token=TEL_BOT_TOKEN)

        # Sending messages
        with client:
            client.send_message(USERNAME, msg)

        LOGGER.debug("Sent item via telegram message.")

    except Exception as err:

        LOGGER.error(f"Failed sending telegram message.", exc_info=err)
