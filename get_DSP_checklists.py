import json
import requests
import os
from datetime import date

# Get checklists from DSP endpoint
# (submission.ebi.ac.uk is down. use submission-test instead)
checklists = requests.get("https://submission-test.ebi.ac.uk/api/checklists?size=300").json()

numberOfChecks = len(checklists['_embedded']['checklists'])

updateTime = date.today().strftime("%Y%m%d")
loc = 'DSP_checklists'
summaryFile = str(updateTime + '_checklists_summary.csv')

try:
    os.stat(loc)
except:
    os.mkdir(loc)


with open(loc+'/'+summaryFile, "a+") as f:
    f.write(str(["ID","name","data type", "description", "update"])[1:-1]+'\n')
    for i in range(numberOfChecks):
        content = checklists['_embedded']['checklists'][i]

        ID = checklists['_embedded']['checklists'][i]['id']
        dataType = checklists['_embedded']['checklists'][i]['dataTypeId']
        name = checklists['_embedded']['checklists'][i]['displayName']

        if 'description' in checklists['_embedded']['checklists'][i].keys():
            description = checklists['_embedded']['checklists'][i]['description']
        else:
            description = 'N/A'

        summary = [str(i+1),ID,name,dataType,description,updateTime]
        f.write(str(summary)[1:-1]+'\n')

        with open(loc+'/'+ID+'.json','w+') as g:
            json.dump(content,g)


