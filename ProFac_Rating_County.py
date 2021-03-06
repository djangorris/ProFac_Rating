import glob
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as mpatches
from matplotlib import style
import numpy as np
import os
import re
from matplotlib.ticker import MaxNLocator
'''
The SERFF .xlsm files should be downloaded into a directory within
the current working directory named "networks". And the file
name should be Carrier_Name.xlsm -- Using underscores for spaces.
'''
'''
Full alphabetical list of counties to compare. The script will loop over all
counties included in the list and create a bar plot for each county.
['Sedgwick','Summit','Teller','Washington','Weld','Yuma']
'''
counties = ['Sedgwick','Summit','Teller','Washington','Weld','Yuma']
### loop counties ###
for county in counties:
	# empty dict to fill with Carrier Name and Rating later
	plot_dict = {}
	# printing html for posting to Colorado Health Insurance Insider
	print(county + ' County Colorado Individual Market Network Size Rating Based on SERFF Data') #Blog Title
	print('<h4>Per Carrier Breakdown</h4>')
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
		# Filter providers by county(ies)
		providers = providers[providers.County == county]
		# Filter facilities by county(ies)
		facilities = facilities[facilities.County == county]
		# Count unique providers
		unique_providers = providers.NPI.nunique()
		# Count unique facilities and pharmacies
		unique_facilities = facilities.NPI.nunique()
		if (file == 'networks/Cigna.xlsm') or (file == 'networks/Anthem_Sm_Group.xlsm'):
			providers2 = pd.read_excel(file,
		            sheetname='IndividualProviders2',
		            header=1,
		            parse_cols = [0,12],
		            )
			facilities2 = pd.read_excel(file,
			            sheetname='Facilities&Pharmacies2',
			            header=1,
			            parse_cols = [0,7],
			            )
			providers2.columns = ['NPI','County']
			facilities2.columns = ['NPI','County']
			# Filter providers by county(ies)
			providers2 = providers2[providers2.County == county]
			# Filter facilities by county(ies)
			facilities2 = facilities2[facilities2.County == county]
			# Count unique providers
			unique_providers2 = providers2.NPI.nunique()
			# Count unique facilities and pharmacies
			unique_facilities2 = facilities2.NPI.nunique()
			# Sum unique1 and unique2
			unique_providers = unique_providers + unique_providers2
			unique_facilities = unique_facilities + unique_facilities2
		# Sum unique providers and unique facilities/pharmacies to get overall "ProFac Rating"
		County_ProFac_Rating = unique_providers + unique_facilities
		print('<h5>' + carrier_name + '</h5>')
		print('<ul><li>' + carrier_name + ' has ' + str(unique_providers) + ' unique providers in ' + county + ' County.</li>')
		print('<li>' + carrier_name + ' has ' + str(unique_facilities) + ' unique facilities in ' + county + ' County.</li>')
		print('<li>' + carrier_name + ' has ' + str(County_ProFac_Rating) + 
				' total unique providers + facilities in ' + county + ' County.</li></ul>')
		## Update dict ##
		plot_dict[carrier_name] = [County_ProFac_Rating]
	## Make Dataframe ##
	df = pd.DataFrame(plot_dict).T
	print('Totals By Carrier for ' + county + ' County')
	print(df)
	# PLOT #
	style.use('fivethirtyeight')
	col = ['darkblue','r','g','c','royalblue','m','goldenrod']
	#
	df.plot(kind='bar', color=col, legend=None)
	plt.ylabel('Unique Providers and\nFacilities/Pharmacies')
	plt.title(county + ' County 2017 Network Size Measured In Unique\n"IndividualProviders" and "Facilities&Pharmacies" Based on SERFF Data')
	# get axis to force whole numbers on y-axis
	ax = plt.gca()
	# force whole numbers on y-axis
	ax.yaxis.set_major_locator(MaxNLocator(integer=True))
	plt.grid(True)
	plt.subplots_adjust(left=0.09, bottom=0.19, right=0.95, top=0.88)
	plt.show()