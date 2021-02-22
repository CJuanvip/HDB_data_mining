import numpy as np
import pandas as pd
import json
import requests
import re
import os
from datetime import datetime as dt
from pandas.io.json import json_normalize
import geocoder
import matplotlib.pylab as plt
import seaborn as sns



url1 = 'https://data.gov.sg/api/action/datastore_search?resource_id=42ff9cfe-abe5-4b54-beda-c88f9bb438ee'
url2 = 'https://data.gov.sg/api/action/datastore_search?resource_id=1b702208-44bf-4829-b620-4615ee19b57c'
url3 = 'https://data.gov.sg/api/action/datastore_search?resource_id=83b2fc37-ce8c-4df4-968b-370fd818138b'
url4 = 'https://data.gov.sg/api/action/datastore_search?resource_id=8c00bf08-9124-479e-aeca-7cc411d884c4'
url5 = 'https://data.gov.sg/api/action/datastore_search?resource_id=adbbddd3-30e2-445f-a123-29bee150a6fe'
urls = [url1, url2, url3, url4, url5]

df_init = pd.DataFrame()
for url in urls:
    result = requests.get(url).json()['result']
    url = url + '&limit={}'.format(result['total'])
    df_init = df_init.append(pd.DataFrame(requests.get(url).json()['result']['records']))

print(len(df_init))