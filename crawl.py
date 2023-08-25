import requests
import pandas as pd
import json

def get_headers():
    return {"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
	"Accept-Encoding" : "gzip, deflate, br",
	"Accept-Language" : "en-US,en;q=0.7",
	"Cache-Control" : "max-age=0",
	"Cookie" : "A1=d=AQABBIWk6GQCENi6iSwe2MwcNxwtOnMx05YFEgEBAQH26WTyZCXcxyMA_eMAAA&S=AQAAAl_p58vdlHGag6mN2TdInII; A3=d=AQABBIWk6GQCENi6iSwe2MwcNxwtOnMx05YFEgEBAQH26WTyZCXcxyMA_eMAAA&S=AQAAAl_p58vdlHGag6mN2TdInII; A1S=d=AQABBIWk6GQCENi6iSwe2MwcNxwtOnMx05YFEgEBAQH26WTyZCXcxyMA_eMAAA&S=AQAAAl_p58vdlHGag6mN2TdInII&j=WORLD; PRF=t%3DAAPL",
	"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
            

url = 'https://query2.finance.yahoo.com/v1/test/getcrumb'
headers = get_headers()

response = requests.get(url, headers=get_headers(), timeout=30)

crumb = response.text

url2 = 'https://query1.finance.yahoo.com/v7/finance/quote?formatted=true&crumb=' + crumb + '&lang=en-US&region=US&symbols=AAPL'

response2 = requests.get(url2, headers=get_headers(), timeout=30)

# json string                                                                                                                
s = '{"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"x","row2":"y","row3":"z"}}'

# read json to data frame    
res = response2.json()
df = pd.read_json(json.dumps(res['quoteResponse']['result'])) 