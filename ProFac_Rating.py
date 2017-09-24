import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
from matplotlib import style
import numpy as np
import os
import re
'''
The SERFF .xlsm files should be downloaded into a directory within
the current working directory named "networks". And the file
name should be Carrier_Name.xlsm -- Using underscores for spaces.
'''
# empty dict to fill with Carrier Name and Rating later
plot_dict = {}
# loop files in /networks
for file in glob.glob('networks/*.xlsm'):
	ext_removed = file.replace('.xlsm','')
	carrier_var = ext_removed.replace('networks/','')
	carrier_name = carrier_var.replace('_',' ')
	# Parse all providers
	providers = pd.read_excel(file,
		            sheetname='IndividualProviders1',
		            header=1,
		            parse_cols = [0,12],
		            )
	# Parse all facilities and pharmacies
	facilities = pd.read_excel(file,
		            sheetname='Facilities&Pharmacies1',
		            header=1,
		            parse_cols = [0,7],
		            )
	providers.columns = ['NPI','County']
	facilities.columns = ['NPI','County']
	# Count unique providers
	unique_providers = providers.NPI.nunique()
	# printing for sanity check
	print(carrier_name + ' has ' + str(unique_providers) + ' unique providers in Colorado')
	# Count unique facilities and pharmacies
	unique_facilities = facilities.NPI.nunique()
	# printing for sanity check
	print(carrier_name + ' has ' + str(unique_facilities) + ' unique facilities in Colorado')
	# Sum unique providers and unique facilities/pharmacies to get overall "ProFac Rating"
	ProFac_Rating = unique_providers + unique_facilities
	# printing for sanity check
	print(carrier_name + ' has ' + str(ProFac_Rating) + 
			' total unique providers + facilities in Colorado\n')
	## Update dict ##
	plot_dict[carrier_name] = [ProFac_Rating]
## Make Dataframe ##
df = pd.DataFrame(plot_dict).T
print('Colorado Totals By Carrier')
print(df)
########
# PLOT #
########
style.use('fivethirtyeight')
col = ['darkblue','r','g','c','royalblue','m','goldenrod']
#
df.plot(kind='bar', color=col, legend=None)
plt.ylabel('Unique Providers and\nFacilities/Pharmacies')
plt.title('Colorado 2017 Network Size Measured In Unique\n"IndividualProviders" and "Facilities&Pharmacies" Based on SERFF Data')
plt.grid(True)
plt.show()