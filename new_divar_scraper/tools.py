"""Helper functions"""
from datetime import datetime
from time import sleep


def zzz():
    now = datetime.now()
    if now.hour == 23 or 9 >= now.hour >= 0:
        sleep(3600)
    else:
        sleep(60)
