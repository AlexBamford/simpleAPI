
import json
import urllib

Extractor = "22b6a603-731b-449c-bfcb-dbd580aedd8f"
apikey = open("apikey.txt")
apikey = apikey.read()


urlList= open("URLs.txt").readlines()

statusResults = open('statusResults.txt','w')
jsondata = open('jsonData.json','w')
errors = open('errors.txt','w')
count = 0
for url in urlList:
    try:
        url = urllib.quote(url)
        query = "https://extraction.import.io/query/extractor/"+Extractor+"?_apikey="+apikey+"&url="+url
        # print query
        count += 1
        data = urllib.urlopen(query).read()
        info = json.loads(data)
        prettyInfo = json.dumps(info, indent=4, sort_keys=True)
        statusCode = info['pageData']['statusCode']
        resourceId = info['pageData']['resourceId']
        sourceUrl = info['url']

        print "\n", sourceUrl
        print statusCode
        print resourceId, "\n"
        output = (sourceUrl, statusCode, resourceId)
        textoutput = sourceUrl+str(statusCode)+resourceId
        statusResults.write(textoutput)
        jsondata.write(prettyInfo)
    except Exception as e:
        print e
        print info
        errors.write(info)
        continue
output.close()
errors.close()
statusResults.close()
    # for line in result:
    #     pageNumber = 1
    #     url2 = line['Link'][0]['href']
    #     totalItems = line[totalItemsColumnName][0]['text']
    #     #print url2 + str(totalItems)
    #     items = 0
    #     while items < int(totalItems):
    #         newUrl = url2+paginationParameter+str(pageNumber)+"\n"
    #         pageNumber += 1
    #         items += itemsPerPage
    #         print newUrl
    #         output.write(newUrl)
    # output.close()
