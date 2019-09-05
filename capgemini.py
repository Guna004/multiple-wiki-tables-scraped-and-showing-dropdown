from flask import Flask,render_template
import urllib 
import requests
import pandas as pd
from bs4 import BeautifulSoup

from urllib.request import urlopen

def table():
    data=[]
    url = "https://en.wikipedia.org/wiki/Capgemini"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table=soup.find('table',{'class':'infobox vcard'})
    rows=table.find_all('tr')
    for row in rows:
        data.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th', 'td'])])

    df = pd.DataFrame(data[11:16],columns=data[2])
    export_csv = df.to_csv (r'/home/dev732/newproj/venv/company 004/capgemini.csv', index = None, header=True) 
    
    return df.to_html(header="true", table_id="table")

