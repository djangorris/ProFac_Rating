import pandas as pd

file = 'Anthem.xlsm'
# Parse all providers
providers = pd.read_excel('networks/' + file,
	            sheetname='IndividualProviders1',
	            header=1,
	            parse_cols = 'A',
	            names=['NPI'])
# Parse all facilities and pharmacies
facilities = pd.read_excel('networks/' + file,
	            sheetname='Facilities&Pharmacies1',
	            header=1,
	            parse_cols = 'A',
	            names=['NPI'])
# Count unique providers
unique_providers = providers.NPI.nunique()
# Count unique facilities and pharmacies
unique_facilities = facilities.NPI.nunique()
# Sum unique providers and unique facilities/pharmacies to get overall "FacPro Rating"
FacPro_Rating = unique_providers + unique_facilities
print(str(FacPro_Rating) + ' total unique providers + facilities.')