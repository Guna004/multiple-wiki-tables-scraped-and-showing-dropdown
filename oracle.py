from flask import Flask,render_template
import urllib 
import requests
import pandas as pd
from bs4 import BeautifulSoup

from urllib.request import urlopen
app = Flask(__name__)
from urllib.request import urlopen
@app.route('/oracle')
def oracle():
    data3=[]
    url3 = "https://en.wikipedia.org/wiki/Oracle_Corporation"
    page3 = requests.get(url3)
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    table=soup3.find('table',{'class':'infobox vcard'})
    rows3=table.find_all('tr')
    for row in rows3:
        data3.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th', 'td'])])

    df3 = pd.DataFrame(data3[13:19],columns=data3[2])
    export_csv = df3.to_csv (r'/home/dev732/newproj/venv/company 004/oracle.csv', index = None, header=True) 
    return df3.to_html(header="true", table_id="table")

