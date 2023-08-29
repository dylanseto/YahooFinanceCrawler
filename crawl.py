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

# read json to data frame    
res = response2.json()
df = pd.json_normalize(res['quoteResponse']['result'])

url3 = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/AAPL?formatted=true&crumb=' + crumb + '&modules=summaryProfile'

response4 = requests.get(url3, headers=get_headers(), timeout=30)
res2 = response4.json()

df2 = pd.json_normalize(res2['quoteSummary']['result'][0]['summaryProfile'])