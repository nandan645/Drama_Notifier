import time
import requests

update= open('/home/user/Path_to_folder/Drama_Notifier/firstScrape', 'r').read()

time_now=time.ctime()

Bot_API_Token = "your bot token"
Chat_Group_Id = "your chat group id"

base_url= 'https://api.telegram.org/bot'+Bot_API_Token+'/sendMessage?chat_id='+Chat_Group_Id+'&text={}'.format(time_now+update)

requests.get(base_url)
