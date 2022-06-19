import requests
from bs4 import BeautifulSoup
from img2dataset import download
import shutil
import os
 
url = 'https://redive.estertion.win/card/full/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    # print(link.get('href'))
    output_dir = os.path.abspath("/public/images/cards")
  
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    download(
        processes_count=16,
        thread_count=32,
        url_list=urls,
)
