import json
import requests
import sys

# Content required for Elastic Search API calls

elasticSearchAPIendpoint = "https://#accountnumber/es.amazon.com/"
authorizationHeaders = {
  "Authorization": "Basic #Auth"
  "Content-Type": "application/json"
}
createIndexPayload = {}

if not sys.argv[1]:
  sys.exit("This script requires first argument as the index name to be created")
else:
  indexName = sys.argv[1]
  print("Index Name is received as: "+indexName)
  
  createIndexResponse = requests.request("PUT",elasticSearchAPIendpoint,headers=authorizationHeaders,body=createIndexPayload
  
  if createIndexResponse.status_code in [200,201]:
    print("Index Created Successfully!")
    sys.exit(0)
  else:
    print("Index Creation Failed")
    print("Status Code is: "+createIndexResponse.status_code)
    sys.exit("Result: Unsuccessful Creation API")

