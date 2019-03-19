# Create connection 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

# Download page

raw_data = conn.read()
html_content = raw_data.decode("utf-8")

# print(html_content)

# Find ROI

soup = BeautifulSoup(html_content, "html.parser")

table_title = soup.find("table", id="tblGridData")
title_col   = table_title.find_all("td", "h_t") 
title_list = [""]
for col in title_col:
    title_list.append(col.string)

table_content = soup.find("table", id="tableContent")
rows_list = table_content.find_all("tr")
excel_table = []
for row in rows_list:
    cell_list = row.find_all("td", "b_r_c")
    if len(cell_list) != 0:
        cell_list.pop()
    cell_list_content = []
    for index, item in enumerate(cell_list):
        cell_list_content.append(item.string)
    excel_table.append(dict(zip(title_list, cell_list_content)))

#print(excel_table)
    

pyexcel.save_as(records = excel_table, dest_file_name = "vinamilk.xlsx")