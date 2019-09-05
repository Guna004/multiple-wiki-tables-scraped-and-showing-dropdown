from flask import Flask,render_template
import urllib 
import requests
import pandas as pd
from bs4 import BeautifulSoup

from urllib.request import urlopen

def ibm():
    data2=[]
    url2 = "https://en.wikipedia.org/wiki/IBM"
    page2 = requests.get(url2)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    table=soup2.find('table',{'class':'infobox vcard'})
    rows2=table.find_all('tr')
    for row in rows2:
        data2.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th', 'td'])])

    df2 = pd.DataFrame(data2[13:19],columns=data2[2])
    export_csv = df2.to_csv (r'/home/dev732/newproj/venv/company 004/ibm.csv', index = None, header=True) 
    return df2.to_html(header="true", table_id="table")

  


