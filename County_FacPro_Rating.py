import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
from matplotlib import style
import numpy as np
import os
import re

```
The SERFF .xlsm files should be downloaded into a directory within
the current working directory named "networks". And the file
name should be Carrier_Name.xlsm -- Using underscores for spaces.
```

# Create dictionary {'Carrier Name': 'networks/Carrier_Name.xlsm', 'Etc':'networks/Etc.xlsm'}
carrier_dict = {}
for file in glob.glob('networks/*.xlsm'):
	carrier_name = file.replace('.xlsm','')
	carrier_name = carrier_name.replace('networks/','')
	carrier_name = carrier_name.replace('_',' ')
	carrier_dict.update({carrier_name: file})
print(carrier_dict)

# Carriers to compare
data = np.array([['Carrier Label', 'Filename', 'Size'],
                ['Anthem BCBS','Anthem.csv',anthem_],
                ['Bright',7507],
                ['Cigna',13550],
                ['Kaiser',13391],
                ['CO Choice',5711],
                ['Denver Health',858],
                ['RMHP',11672]])
# County to compare
county = 'Denver'
# Parse all providers
providers = pd.read_excel('networks/' + file,
	            sheetname='IndividualProviders1',
	            header=1,
	            parse_cols = [0,12],
	            )
providers.columns = ['NPI','County']
# Parse all facilities and pharmacies
facilities = pd.read_excel('networks/' + file,
	            sheetname='Facilities&Pharmacies1',
	            header=1,
	            parse_cols = [0,7],
	            )
facilities.columns = ['NPI','County']
# Filter providers by county(ies)
providers = providers[providers.County == county]
# Filter facilities by county(ies)
facilities = facilities[facilities.County == county]
# Count unique providers
unique_providers = providers.NPI.nunique()
# printing for sanity check
print(str(unique_providers) + ' unique providers')
# Count unique facilities and pharmacies
unique_facilities = facilities.NPI.nunique()
# printing for sanity check
print(str(unique_facilities) + ' unique facilities')
# Sum unique providers and unique facilities/pharmacies to get overall "FacPro Rating"
County_FacPro_Rating = unique_providers + unique_facilities
print(str(County_FacPro_Rating) + ' total unique providers + facilities.')