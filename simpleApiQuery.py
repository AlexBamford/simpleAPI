#!/usr/bin/python
import json
import urllib
import time
import datetime


t = (time.strftime("%d-%m-%Y_%H:%M:%S-%Z"))
Extractor = "22b6a603-731b-449c-bfcb-dbd580aedd8f"
apikey = open("apikey.txt")
apikey = apikey.read()


urlList= open("URLs.txt").readlines()

statusResults = open('statusResults_'+t+'.txt','w')
jsondata = open('jsonData_'+t+'.json','w')
errors = open('errors_'+t+'.txt','w')
count = 0
for url in urlList:
    try:
        encodedurl = urllib.quote(url)
        query = "https://extraction.import.io/query/extractor/"+Extractor+"?_apikey="+apikey+"&url="+encodedurl
        # print query
        count += 1
        data = urllib.urlopen(query).read()
        info = json.loads(data)
        prettyInfo = json.dumps(info, indent=4, sort_keys=True)
        statusCode = info['pageData']['statusCode']
        resourceId = info['pageData']['resourceId']
        sourceUrl = info['url']
        timestamp = info['pageData']['timestamp']
        timestamp = str(timestamp)[:10]

        d = datetime.datetime.fromtimestamp(int(timestamp)).strftime('%a %Y-%m-%d %H:%M:%S')
        #
        print "\n", sourceUrl
        print statusCode
        print resourceId, "\n"
        output = (sourceUrl, statusCode, resourceId)
        textoutput = str(statusCode)+", "+d+", "+resourceId+", "+sourceUrl+" \n"
        statusResults.write(textoutput)
        jsondata.write(prettyInfo)
    except Exception as e:
        print e
        print "Error!"
        print prettyInfo
        print str(timestamp)[:10]
        errors.write("\n"+url+"\n"+prettyinfo)     
        continue
jsondata.close()
errors.close()
statusResults.close()
