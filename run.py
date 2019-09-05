from flask import Flask,render_template
app = Flask(__name__)

import pandas as pd
import requests
from bs4 import BeautifulSoup

@app.route('/')
def table():
    data=[]
    url = "https://en.wikipedia.org/wiki/Infosys"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table=soup.find('table',{'class':'infobox vcard'})
    rows=table.find_all('tr')
    for row in rows:
        data.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th','td'])])

    df = pd.DataFrame(data[0:],columns=data[2])

    return df.to_html(header="true", table_id="table")


if __name__ == '__main__':
    app.run(debug=True)







