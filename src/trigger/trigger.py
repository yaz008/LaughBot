from os import getenv
from json import load
from pyrogram.client import Client
from pyrogram.types import Message
from typing import Callable

with open(file='src\\trigger\\replace.json',
          mode='r',
          encoding='UTF-8') as replace_file:
    REPLACE: dict[str, str] = load(replace_file)

def trigger(func: Callable[[Message, str], None]) -> Callable[[Client, Message], None]:
    def wrapper(_: Client, message: Message) -> None:
        if message.from_user.id == int(getenv(key='MY_ID')):
            if message.text in REPLACE.keys():
                func(message, REPLACE[message.text])
    return wrapper