# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 15:50:23 2021

@author: broad
"""

from sec_api import FullTextSearchApi
import pandas as pd
import json 
import time
# import urllib.request

Filings = pd.read_excel(
    r'C:\Users\broad\OneDrive\Documents\EXCEL\CommentLetterData.xlsx')

c = Filings['Company']
#c = c.str.slice(0,8,1)  # slice first 8 characters in company
d = Filings['File date']

fullTextSearchApi = FullTextSearchApi(
    api_key="d42bbc254d320b27c0402ffce18df086a507e1be646dd197a7f8dfc24ef054b5")
  # api key is broken and limited to 100 uses for free version. Need to 
  # buy research version. $55 /// 10/12 key purchased
def sec_ext(c):
    for value in range(len(c)):
        try:    
            query = {"query": f'"{c[value]}"',
              "formTypes": ['UPLOAD'],
              "startDate": '2020-01-20',
              "endDate": '2021-07-01',
            }
            
            filings = fullTextSearchApi.get_filings(query)
            
            print(json.dumps(filings, indent=4, sort_keys=True))
            
            # rate limited API workaround
        except:
            continue
ext = sec_ext(c)  

work = pd.read_csv("ext_csv")  
print(work.head())

 # def date_lookup(ext,d):
   # for value in range(len(d)):
      
       
# url = "SEC Text file here"
# file = urllib.request.urlopen(url)

# for line in file:
# 	decoded_line = line.decode("utf-8")
# 	print(decoded_line)      