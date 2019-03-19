# Create connection 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

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

print(song_list)
    
pyexcel.save_as(records = song_list, dest_file_name = "itunes_top_100.xlsx")

