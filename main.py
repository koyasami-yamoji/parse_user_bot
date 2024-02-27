import asyncio
import time

from telethon import TelegramClient
from telethon.tl.functions.messages import GetPeerDialogsRequest

api_id = 123123
api_hash = 'qwe'

client = TelegramClient('bot', api_id=api_id, api_hash=api_hash)


async def main():
	entity = await client.get_entity('https://t.me/lnmanga')
	result = await client(GetPeerDialogsRequest(peers=[entity]))
	count = result.dialogs[0].unread_count
	if count > 0:
		bot_entity = await client.get_entity('https://t.me/parsemanhvaBot')
		all_message = client.iter_messages(entity=entity, limit=count)
		async for message in all_message:
			await client.send_message(bot_entity, message.text)
			await message.mark_read()
			await asyncio.sleep(1)
	else:
		return


with client:
	client.loop.run_until_complete(main())
