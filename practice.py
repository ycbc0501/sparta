from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
music_list = soup.select('#body-content > .newest-list > .music-list-wrap > .list-wrap > tbody > tr')

for music in music_list:
    a_tag = music.select_one('td.info > a')
    if a_tag is not None:
        #rank = music.select_one('td.number').next.strip()
        #rank = music.select_one('td.number').next_element.strip()
        #rank = music.select_one('td.number').contents[0].strip()
        rank = music.select_one('td.number').text[0:2].strip()
        #music.select_one('td.number').span.extract(); rank = music.select_one('td.number').text.strip()
        title = music.select_one('td.info > a.title').text.strip()
        singer = music.select_one('td.info > a.artist').text.strip()
        print(rank,title,singer)