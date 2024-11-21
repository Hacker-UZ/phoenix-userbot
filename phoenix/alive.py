from telethon import events
import phoenix.client
import time
client = phoenix.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.alive'))
async def alive(event):
		client = event.client
		me = await client.get_me()
		username = me.username
		img = await client.download_profile_photo(username)
		time.sleep(0.5)
		await event.respond(f"""Foydalanuvchi: @{username}
Phoenix Userbot: https://t.me/phoenix_userbot

Developer: @programmer_www
			
v.1.3.0

📥 INSTALL 

$ pkg update && pkg upgrade

$ apt update && apt upgrade

$ pkg install git

$ pkg install python

$ git clone https://github.com/Hacker-UZ/phoenix-userbot

$ python setup.py

$ python main.py""", file=img)
		await event.message.delete()