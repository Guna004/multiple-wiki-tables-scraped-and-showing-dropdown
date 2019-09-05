from flask import Flask,render_template
app = Flask(__name__)

import pandas as pd
import requests
from bs4 import BeautifulSoup

@app.route('/')
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

    
    

    data2=[]
    url2 = "https://en.wikipedia.org/wiki/IBM"
    page2 = requests.get(url2)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    table=soup2.find('table',{'class':'infobox vcard'})
    rows2=table.find_all('tr')
    for row in rows2:
        data2.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th', 'td'])])

    df2 = pd.DataFrame(data2[13:19],columns=data2[2])


    data3=[]
    url3 = "https://en.wikipedia.org/wiki/Oracle_Corporation"
    page3 = requests.get(url3)
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    table=soup3.find('table',{'class':'infobox vcard'})
    rows3=table.find_all('tr')
    for row in rows3:
        data3.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th', 'td'])])

    df3 = pd.DataFrame(data3[13:19],columns=data3[2])



    data4=[]
    url4 = "https://en.wikipedia.org/wiki/Microsoft#Financial"
    page4 = requests.get(url4)
    soup4 = BeautifulSoup(page4.content, 'html.parser')
    table=soup4.find('table',{'class':'infobox vcard'})
    rows4=table.find_all('tr')
  
    for row in rows4:
        data4.append([cell.text.replace('\n', ' ')for cell in row.find_all(['th', 'td'])])

    df4 = pd.DataFrame(data4[13:19],columns=data4[2])

    data5=[]
    url5 = "https://en.wikipedia.org/wiki/SAP_SE"
    page5 = requests.get(url5)
    soup5 = BeautifulSoup(page5.content, 'html.parser')
    table=soup5.find('table',{'class':'infobox vcard'})
    rows5=table.find_all('tr')
    for row in rows5:
        data5.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th', 'td'])])

    df5 = pd.DataFrame(data5[10:],columns=data5[2])

    data6=[]
    url6 = "https://en.wikipedia.org/wiki/Accenture#Finances"
    page6 = requests.get(url6)
    soup6 = BeautifulSoup(page6.content, 'html.parser')
    table=soup6.find('table',{'class':'infobox vcard'})
    rows6=table.find_all('tr')
    for row in rows6:
        data6.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th', 'td'])])

    df6 = pd.DataFrame(data6[11:17],columns=data6[2])


    data7=[]
    url7 = "https://en.wikipedia.org/wiki/Tata_Consultancy_Services"
    page7 = requests.get(url7)
    soup7 = BeautifulSoup(page7.content, 'html.parser')
    table=soup7.find('table',{'class':'infobox vcard'})
    rows7=table.find_all('tr')
    for row in rows7:
        data7.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th', 'td'])])

    df7 = pd.DataFrame(data7[10:16],columns=data7[2])

    data8=[]
    url8= "https://en.wikipedia.org/wiki/Cognizant"
    page8 = requests.get(url8)
    soup8 = BeautifulSoup(page8.content, 'html.parser')
    table=soup8.find('table',{'class':'infobox vcard'})
    rows8=table.find_all('tr')
    for row in rows8:
        data8.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th', 'td'])])

    df8 = pd.DataFrame(data8[13:18],columns=data8[2])


    data9=[]
    url9= "https://en.wikipedia.org/wiki/Infosys"
    page9 = requests.get(url9)
    soup9 = BeautifulSoup(page9.content, 'html.parser')
    table=soup.find('table',{'class':'infobox vcard'})
    rows9=table.find_all('tr')
    for row in rows9:
        data9.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th','td'])])

    df9 = pd.DataFrame(data9[11:16],columns=data9[2])



    data10=[]
    url10= "https://en.wikipedia.org/wiki/Hewlett_Packard_Enterprise"
    page10 = requests.get(url10)
    soup10= BeautifulSoup(page10.content, 'html.parser')
    table=soup10.find('table',{'class':'infobox vcard'})
    rows10=table.find_all('tr')
    for row in rows10:
        data10.append([cell.text.replace('\n', ' ')for cell in row.find_all(['tr','th','td'])])

    df10 = pd.DataFrame(data10[10:16],columns=data10[2])
 


    


    return render_template('index.html',tables=[df.to_html(classes='data'),df2.to_html(classes='data'),df3.to_html(classes='data'),df4.to_html(classes='data'),df5.to_html(classes='data'),df6.to_html(classes='data'),df7.to_html(classes='data'),df8.to_html(classes='data'),df9.to_html(classes='data'),df10.to_html(classes='data')],titles = ['Na', 'Capgemini', 'IBM-International Business Machine Data','Oracle','Microsoft Data','SAP','Accenture','TCS','Cognizant','Infosys','HPE'])

  
if __name__ == '__main__':
    app.run(debug=True)

