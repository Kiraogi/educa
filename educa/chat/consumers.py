import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = f'chat_{self.id}'
        # Присоединиться к группе чат-комнаты
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, 
            self.channel_name
            )
        # инять соединение
        self.accept()
    
    def disconnect(self, close_code):
        pass

    # Получить сообщение из WebSocket
    def receive(self, text_data):
        text_data_json = json.load(text_data)
        message = text_data_json
        # Отправить сообщение в WebSocket
        self.send(text_data=json.dumps({'message': message}))

        