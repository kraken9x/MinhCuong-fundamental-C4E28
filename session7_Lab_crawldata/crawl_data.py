# Create connection 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://dantri.com.vn"
conn = urlopen(url)

# Download Page
raw_data = conn.read()
# print(raw_data) # Dữ liệu chưa được làm mịn
html_content = raw_data.decode("utf-8")
# print(html_content)

# Find ROI

soup = BeautifulSoup(html_content, "html.parser")
#print(soup.prettify())

ul = soup.find("ul", "ul1 ulnew") #Nếu là class thì chỉ viết giá trị, nếu khác class thì viết đầy đủ: VD = id = "ul1 ulnew"

# print(ul.prettify())

li_list = ul.find_all("li")
#li = li_list[0]
#print(li.prettify())

# a = li.h4.a 
# #print(a)
# title = a.string
# print(title)
# print(url + a["href"])


a_list_of_dictionaries = []
dic = {}

for li in li_list:
    a = li.h4.a 
    href = a["href"]
    title = a.string
    dic["link"] = href
    dic["title"] = title
    a_list_of_dictionaries.append(dic)

print(a_list_of_dictionaries)    