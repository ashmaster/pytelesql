from telesql import TeleSQL
from start import CreateTeleSQLDB

class TeleObj:
    def __init__(self) -> None:
        self.stringSession = None
        #self.connectionString = 'telesql:1BVtsOLUBu7Irb_AJ4EWRXZwuvPWoA3muqrYx480L7j2FzCxnvn5GjaFzTyn1F-NUUe5BEo7qINpDrLQMp35Uy1m2J7WWsPfHsV0sQ25Jtm0LxnGtCfAhH4b5-k_x13SkV09P6CSoo2lf0NcAJF_Aq3sbo2JXuqditC1M72GSjt1jjlE1VH_ZzgL-7IP9JPdvlMVGvVCmlCRDvDyHmkE1pkFCLEZkFt2xPpr19Tp6fbLyXLSG5DeGHSWbwb7gDLhXRQhT61ecDv6RTTkWWMl_XdJZlgu4TQfDjydTnkNYvYOc2sbBDcZkTVWaKx3HFfPfsu19Yk5JvUUIwyM6f_2r_K87FkDgiak=:db1:1BVtsO'
        [self.client, self.connection] = TeleSQL().connectTele('session') 
            
    def findTable(self,table_name):
        #names =  await CreateTeleSQLDB.getCollections()
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
            
