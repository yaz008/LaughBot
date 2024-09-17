from app import app
from pyrogram.types import Message
from trigger import trigger

@app.on_message(filters=None)
@trigger
def on_trigger(message: Message, replace: str) -> None:
    message.edit_text(text=replace)

if __name__ == '__main__':
    app.run()