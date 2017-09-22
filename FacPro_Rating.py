import pandas as pd

file = 'RMHP--b76994c2-2748-4ba1-b385-a5cb1126f623_DATA_ECP_NETWORK_ADEQUACY.xlsm'
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
print(FacPro_Rating)