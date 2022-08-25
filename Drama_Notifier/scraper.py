import requests
from bs4 import BeautifulSoup

#website_url = "https://watchasian.pe/drama-detail/salvation-interpreter"
website_url = open('/home/user/Path_to_folder/Drama_Notifier/current_drama', 'r').read()

result = requests.get(website_url)
htmlcontent = result.content

domain= (website_url).split('/')[2]

site = BeautifulSoup(htmlcontent, 'html.parser')

latest = site.find(class_="list-episode-item-2 all-episode").find('a')

print(" ")
print(" ")

info = site.find('div', class_="info").get_text(strip=True).split('Status:')[1].partition('Released:')[0]

print('\n'"Status:- ",info,'\n')

Video_name = latest.find('h3', class_="title").text.strip()

Video_url = latest.get('href')

print(Video_name,":-")
print(" ")
print("https://"+domain+Video_url)