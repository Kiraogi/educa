import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Принять соединение
        self.accept()
    
    def disconnect(self, close_code):
        pass

    # Получить сообщение из WebSocket
    def receive(self, text_data):
        text_data_json = json.load(text_data)
        message = text_data_json
        # Отправить сообщение в WebSocket
        self.send(text_data=json.dumps({'message': message}))

        