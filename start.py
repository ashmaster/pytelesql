from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.sessions import StringSession
from telesql import TeleSQL
from telethon.tl.functions.channels import GetFullChannelRequest
import os
api_id = 26725205
api_hash = 'a4bc88912823d011308b761a34dcc831'
dbPath = "C://Users//ashis//pytelesql//db"
class CreateTeleSQLDB: 
    def __init__(self) -> None:
        self.stringSession = None
        #self.connectionString = 'telesql:1BVtsOLUBu7Irb_AJ4EWRXZwuvPWoA3muqrYx480L7j2FzCxnvn5GjaFzTyn1F-NUUe5BEo7qINpDrLQMp35Uy1m2J7WWsPfHsV0sQ25Jtm0LxnGtCfAhH4b5-k_x13SkV09P6CSoo2lf0NcAJF_Aq3sbo2JXuqditC1M72GSjt1jjlE1VH_ZzgL-7IP9JPdvlMVGvVCmlCRDvDyHmkE1pkFCLEZkFt2xPpr19Tp6fbLyXLSG5DeGHSWbwb7gDLhXRQhT61ecDv6RTTkWWMl_XdJZlgu4TQfDjydTnkNYvYOc2sbBDcZkTVWaKx3HFfPfsu19Yk5JvUUIwyM6f_2r_K87FkDgiak=:db1:1BVtsO'
        # [self.client, self.connection] = TeleSQL().connectTele('session')
        # obj = TeleObj()
        # obj.findTable("abc")
    
    async def createClient(self, dbName):
        async with TelegramClient(StringSession(''), api_id, api_hash) as self.client:
            self.stringSession = StringSession.save(self.client.session)
            f = open("session.txt", "w")
            f.write('telesql:'+self.stringSession+':'+dbName+':'+self.stringSession[0:6])
            f.close()
            print('Please use the following string to connect to your telesql')
            print('telesql:'+self.stringSession+':'+dbName+':'+self.stringSession[0:6])

    async def getChannelMessages(self,id): 
        dialogs = await self.client.get_dialogs()
        channel = await self.client.get_entity(id)
        async for message in self.client.iter_messages(channel, search='#123456'):
            print(message.raw_text)


    async def getCollections(self):
        
        dir_list = os.listdir(dbPath)
        print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",dir_list)
        return dir_list


    async def migrateDb(self):
        names =  await self.getCollections()
        chats = await self.getMyChannels()
        print(self.connection['dbName'])
        dbName = self.connection['dbName']
        dbCollections = []
        fileCollections = []
        for channel in chats:
            channelName = channel.name
            if(channelName.startswith('telesql')):
                teleDbName = channelName.split('.')[1]
                if(teleDbName == dbName):
                    dbCollections.append(channelName)

        for filename in names:
            flag = False
            collectionname = 'telesql.' + dbName + '.' + filename.split(".")[0]
            fileCollections.append(collectionname)
            print( "Collection name" , collectionname)
            for channel in chats: 
                if(channel.is_channel):
                    if collectionname == channel.name:
                        print("Already Existing Collection")
                        flag = True
                        break
            if not flag:            
                f = open(dbPath+"//"+filename, "r")
                about = f.read() 
                result = await self.client(functions.channels.CreateChannelRequest(
                    title=collectionname,
                    about=about,
                    megagroup=False,
                ))                       
            

    async def getMyChannels(self): 
        dialogs = await self.client.get_dialogs()
        # for dialog in dialogs:
        #     if(dialog.is_channel):
        #         channelName = dialog.name
        #         print("fffffgdsbvds",channelName)
        #         ch = await self.client.get_entity(channelName)
        #         ch_full = await self.client(GetFullChannelRequest(channel=ch))
        #         print(ch_full.full_chat.about)
        return dialogs

class TeleObj:
    def __init__(self) -> None:
        self.stringSession = None
        #self.connectionString = 'telesql:1BVtsOLUBu7Irb_AJ4EWRXZwuvPWoA3muqrYx480L7j2FzCxnvn5GjaFzTyn1F-NUUe5BEo7qINpDrLQMp35Uy1m2J7WWsPfHsV0sQ25Jtm0LxnGtCfAhH4b5-k_x13SkV09P6CSoo2lf0NcAJF_Aq3sbo2JXuqditC1M72GSjt1jjlE1VH_ZzgL-7IP9JPdvlMVGvVCmlCRDvDyHmkE1pkFCLEZkFt2xPpr19Tp6fbLyXLSG5DeGHSWbwb7gDLhXRQhT61ecDv6RTTkWWMl_XdJZlgu4TQfDjydTnkNYvYOc2sbBDcZkTVWaKx3HFfPfsu19Yk5JvUUIwyM6f_2r_K87FkDgiak=:db1:1BVtsO'
        [self.client, self.connection] = TeleSQL().connectTele('session') 
            
    def findTable(self,table_name):
        chats = CreateTeleSQLDB.getMyChannels()
        print(self.connection['dbName'])
        dbName = self.connection['dbName']
    
        for channel in chats:
            channelName = channel.name
            if(channelName.startswith('telesql.' + dbName)):
                teleChannelName = channelName.split('.')[2]
                if(teleChannelName == table_name):
                    return channel
            
        print("Channel not found")


a = CreateTeleSQLDB()