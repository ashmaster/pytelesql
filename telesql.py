from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.sessions import StringSession

api_id = 26725205
api_hash = 'a4bc88912823d011308b761a34dcc831'
class TeleSQL:

    def __init__(self) -> None:
        self.client = None   
        f = open('session.txt', 'r')
        connectionString= f.read().rstrip()
        f.close()
        connectionArray = connectionString.split(':')
        if(connectionArray[0]!='telesql'):
            assert NameError
        connection = {'stringSession': connectionArray[1], 'dbName': connectionArray[2], 'dbIndex': connectionArray[3]}
        print(connection)
        client = TelegramClient(StringSession(connection['stringSession']), api_id, api_hash)
        client.start() 
