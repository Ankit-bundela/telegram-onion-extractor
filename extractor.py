from telethon.sync import TelegramClient
import time
import re

api_id=23775792
api_hash='850ddd12daaa3da9f1e4b4132bdd6037'
client=TelegramClient('anon', api_id, api_hash)

async def main():
	channel_username = 'toronionlinks'  #Replace with actual Telegram username
	try:
		print(f"Fetching messages from channel: {channel_username} ...")
		print("-"*70)
		link_found = False
		async for message in client.iter_messages(channel_username, limit=100):
			if message.text:
				onion_links = re.findall(r'(https?://[^\s]*\.onion[^\s]*)', message.text)
				if onion_links:
					link_found = True
					for link in onion_links:
						time.sleep(.23)
						print(link)
		if not link_found:
			print("No .onion links found in the last 100 messages.")
	except Exception as e:
		print(f"Error: {str(e)}")
with client:
	client.loop.run_until_complete(main())
