# In emergency/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EmergencyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        latitude = data['latitude']
        longitude = data['longitude']
        # Save or process the data as needed
        await self.send(text_data=json.dumps({
            'message': 'Emergency data received'
        }))
