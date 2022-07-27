import os
import pandas as pd
import requests
import json
import time

# import api key from enviroment varialbe 
APIKEY = os.environ['APIKEY']


counties = ["Multnomah","Clackamas","Washington"]
assessor_data = pd.DataFrame()
for county in counties:
    is_data = True
    page = 1
    while is_data:
        response = pd.DataFrame(requests.get("https://www.portlandmaps.com/api/assessor.cfm?download=0&api_key={}&format=json&sort_field=address&sort_order=ASC&action=assessor&search_type=basic&debug=0&address=&property_id=&state_id=&neighborhood=&city=&county={}&alt_account_number=&zip_code=&legal_description=&page={}&count=1000".format(APIKEY,county,page)).json()['results'])
        is_data = not response.empty
        print(response)
        print (is_data)
        print (response.size)
        response.to_csv("Portland_Maps_Assessor_Data.csv", mode='a', index=False, header=not os.path.exists("Portland_Maps_Assessor_Data.csv"))

        page += 1
        time.sleep(5)
os.rename ("Portland_Maps_Assessor_Data.csv", "/data/Portland_Maps_Assessor_Data.csv")