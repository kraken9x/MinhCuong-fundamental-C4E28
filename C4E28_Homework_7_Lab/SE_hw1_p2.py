# Create connection 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL


url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)

# Download page

raw_data = conn.read()
html_content = raw_data.decode("utf-8")

# print(html_content)

# Find ROI

soup = BeautifulSoup(html_content, "html.parser")

section = soup.find("section", "chart-grid")
div = section.find("div", "section-content")
ul = div.find("ul")
li_list = ul.find_all("li")

song_list = []

for li in li_list:
    song_name = li.h3.a.string
    artist = li.h4.a.string
    song = {
        "title" : song_name,
        "artist" : artist
    }
    song_list.append(song)

#print(song_list)
    
#pyexcel.save_as(records = song_list, dest_file_name = "itunes_top_100.xlsx")

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
song_1 = song_list[0]
title = song_1["title"]
artist_name = song_1["artist"]
search_song = title + " - " + artist_name
#print(search_song)
dl.download([search_song])