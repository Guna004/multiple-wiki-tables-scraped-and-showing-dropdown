from flask import Flask,render_template
app = Flask(__name__)

import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

@app.route('/capgemini')
def capgemini():
    os.system('python capgemini.py')

    df=pd.read_csv('/home/dev732/newproj/venv/company 004/capgemini.csv')

    return render_template('index.html',tables=[df.to_html(classes='data')],titles = ['Na','capgemini'])
    
@app.route('/ibm')
def ibm(): 

    os.system('python ibm.py')
    
    df2=pd.read_csv('/home/dev732/newproj/venv/company 004/ibm.csv')

    return render_template('index.html',tables=[df2.to_html(classes='data')],titles = ['Na','ibm'])

@app.route('/oracle')
def oracle():
    os.system('python oracle.py')
    
    df3=pd.read_csv('/home/dev732/newproj/venv/company 004/oracle.csv')



    return render_template('index.html',tables=[df3.to_html(classes='data')],titles = ['Na','Oracle'])


@app.route('/')
def main():

    return render_template('main.html')

  
if __name__ == '__main__':
    app.run(debug=True)

