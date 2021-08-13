import requests
from bs4 import BeautifulSoup

file_xuhao = 120

web_url = 'https://e-shuushuu.net/search/results/?page=9&tags=136693'
r = requests.get(web_url)
all_a = BeautifulSoup(r.text, 'lxml').find_all('a', class_='thumb_image')
for a in all_a:
  img_url ='https://e-shuushuu.net' + a['href']
  print(img_url)
  file_name ='F:\\PYproject\\img\\' + str(file_xuhao) + '.png'
  print(file_name)
  f = requests.get(img_url)
  with open(file_name, "wb") as code:
    code.write(f.content)
  file_xuhao = file_xuhao + 1

