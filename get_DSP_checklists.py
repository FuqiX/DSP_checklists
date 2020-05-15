import json
import requests
import os
from datetime import date
import pandas as pd

# Get validation schemas  from DSP endpoint
schemas = requests.get("https://submission.ebi.ac.uk/api/validationSchemas?size=100").json()

numberOfChecks = len(schemas['_embedded']['validationSchemas'])

updateTime = date.today().strftime("%Y%m%d")
summaryFile = 'validationSchema_summary.tsv'


all_summary = []
for i in range(numberOfChecks):
    content = schemas['_embedded']['validationSchemas'][i]

    ID = schemas['_embedded']['validationSchemas'][i]['id']
    dataType = schemas['_embedded']['validationSchemas'][i]['dataTypeId']
    name = schemas['_embedded']['validationSchemas'][i]['displayName']

    if 'description' in schemas['_embedded']['validationSchemas'][i].keys():
        description = schemas['_embedded']['validationSchemas'][i]['description']
        # remove \t in the description
        description = description.replace("\t"," ")
    else:
        description = 'N/A'

    # generate seperate file for each validation schema
    with open(ID+'.json','w+') as g:
        json.dump(content,g)

    summary = [ID,name,dataType,description,updateTime]
    all_summary.append(summary)

df = pd.DataFrame(all_summary)
df.columns = ["ID","name","dataType","description","updateTime"]
df.to_csv(summaryFile,sep = "\t")

        



