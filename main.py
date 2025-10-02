```python
from bale import BaleBot

TOKEN = "732980839:3Un4tVhJls1Yhak25BXdrDJVMi6A0-ylVyU"

bot = BaleBot(token=TOKEN)

@bot.on_message
def handle_message(message):
    bot.send_message(message.chat_id, f"📩 شما گفتید: {message.text}")

bot.run()
```
