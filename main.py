import pandas as pd
import requests
import json

url = "https://api.publicapis.org/entries"

payload = dict()
headers = dict()

response = json.loads(requests.request("GET", url, headers=headers, data=payload).text)

apiList = []
descList = []
authList = []
httpsList = []
corsList = []
linkList = []
catList = []
for i in response['entries']:
    apiList.append(i['API'])
    descList.append(i['Description'])
    authList.append(i['Auth'])
    httpsList.append(i['HTTPS'])
    corsList.append(i['Cors'])
    linkList.append(i['Link'])
    catList.append(i['Category'])

csvDataDict = {'API': apiList, 'Description': descList, 'Auth': authList, 'HTTPS': httpsList, 'Cors': corsList, 'Link': linkList, 'Category': catList}
df = pd.DataFrame(csvDataDict)
df.to_csv("output.csv", index=False)
