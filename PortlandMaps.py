import os
import pandas as pd
import requests
import json
import time

# import api key from enviroment varialbe 
APIKEY = os.environ['APIKEY']


counties = ["Clackamas","Clackamas","Washington"]
assessor_data = pd.DataFrame()

for county in counties:
    is_data = True
    page = 1
    while is_data:
        response = pd.DataFrame(requests.get("https://www.portlandmaps.com/api/assessor.cfm?download=0&api_key={}&format=json&sort_field=address&sort_order=ASC&action=assessor&search_type=basic&debug=0&address=&property_id=&state_id=&neighborhood=&city=&county={}&alt_account_number=&zip_code=&legal_description=&page={}&count=1000".format(APIKEY,county,page)).json()['results'])
        print(response)
        assessor_data = assessor_data.append(response)
        is_data = not response.empty
        print (is_data)
        print (assessor_data.size)
        page += 1
        time.sleep(5)
        assessor_data.to_csv("/app/Portland_Maps_Assessor_Data.csv")
assessor_data.to_csv("/data/Portland_Maps_Assessor_Data.csv")