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
    table=soup.find('table',{'class':'wikitable'})
    rows=table.find_all('tr')
    for row in rows:
        data.append([cell.text.replace('\n', ' ')for cell in row.find_all(['th', 'td'])])

    df = pd.DataFrame(data[1:],columns=data[0])

    
    data1=[]
    url1="https://en.wikipedia.org/wiki/Oracle_Corporation"
    page1 = requests.get(url1)
    soup1 = BeautifulSoup(page1.content, 'html.parser')
    table=soup1.find('table',{'class':'wikitable float-left'})
    rows1=table.find_all('tr')
    for row in rows1:
        data1.append([cell.text.replace('\n', ' ')for cell in row.find_all(['th', 'td'])])

    df1 = pd.DataFrame(data1[1:],columns=data[0])

    data2=[]
    url2 = "https://en.wikipedia.org/wiki/IBM"
    page2 = requests.get(url2)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    table=soup2.find('table',{'class':'wikitable float-left'})
    rows2=table.find_all('tr')
    for row in rows2:
        data2.append([cell.text.replace('\n', ' ')for cell in row.find_all(['th', 'td'])])

    df2 = pd.DataFrame(data2[1:],columns=data2[0])


    data3=[]
    url3 = "https://en.wikipedia.org/wiki/Accenture#Finances"
    page3 = requests.get(url3)
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    table=soup3.find('table',{'class':'wikitable float-left plainrowheaders'})
    rows3=table.find_all('tr')
    for row in rows3:
        data3.append([cell.text.replace('\n', ' ')for cell in row.find_all(['th', 'td'])])

    df3 = pd.DataFrame(data3[1:],columns=data3[0])



    data4=[]
    url4 = "https://en.wikipedia.org/wiki/Microsoft#Financial"
    page4 = requests.get(url4)
    soup4 = BeautifulSoup(page4.content, 'html.parser')
    table=soup4.find('table',{'class':'wikitable float-left'})
    rows4=table.find_all('tr')
  
    for row in rows4:
        data4.append([cell.text.replace('\n', ' ')for cell in row.find_all(['th', 'td'])])

    df4 = pd.DataFrame(data4[1:],columns=data4[0])

    data5=[]
    url5 = "https://en.wikipedia.org/wiki/Accenture#Finances"
    page5 = requests.get(url5)
    soup5 = BeautifulSoup(page5.content, 'html.parser')
    table=soup5.find('table',{'class':'infobox vcard'})
    rows5=table.find_all('tr')
    for row in rows5:
        data5.append([cell.text.replace('\n', ' ')for cell in row.find_all(['th', 'td'])])

    df5 = pd.DataFrame(data5[11:16],columns=data5[1])



    return render_template('index.html',tables=[df.to_html(classes='data'),df1.to_html(classes='data'),df2.to_html(classes='data'),df3.to_html(classes='data'),df4.to_html(classes='data'),df5.to_html(classes='data')],titles = ['Na','Infosys Data', 'Oracle Corporation Data', 'IBM-International Business Machine Data','Accenture Data','Microsoft Data','Inbo Box'])

  
if __name__ == '__main__':
    app.run(debug=True)

