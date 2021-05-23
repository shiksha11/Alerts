import requests
import json
import scrapy
import price_spider
from price_spider import PriceSpiderSpider
BASE_URL = "https://apistaging.revmeup.in/api/v1"


# Obtaining Token for API
url = BASE_URL +  "/user/login"
response = requests.post(url, json={
        "userid": "ZKh5adE6Lvb2lQGrru9LEKWQUXq2",
        "password": "ZKh5adE6Lvb2lQGrru9LEKWQUXq2"
})
#print(response)
a = response.json()
token  = a['token']


header = {'Authorization': 'Bearer ' + token, 'content-type': "application/json"}
request_url = BASE_URL +  '/priceAlerts/count' 
l = requests.get(request_url, headers=header)

total_products = l.json()['count']

#covering 100 products in a single for loop
#so total required objects  = total_products/100 + 1 

if (total_products%100 == 0):
        req_loops = total_products//100
else:
        req_loops = total_products//100 + 1

for i in range(1):
        request = BASE_URL + "/priceAlerts"
        p = requests.get(request, headers=header)
        data = p.json()
        for product in data:
                for store in product['stores']:
                        store_link = store['storeLink']
                        
                        store_price = store['storePrice']
                        obj = PriceSpiderSpider()
                        if store_link is not None:
                                obj.start_request(store_link)
                        
                        #ans = obj.amazon_parser()
                        #print(ans)












