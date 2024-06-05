import json
from channels.generic.websocket import AsyncWebsocketConsumer

class UpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "updates",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "updates",
            self.channel_name
        )

    async def send_update(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
        }))
