import pandas as pd
#
file = 'Anthem--8bfa9e3b-d95b-40ca-8228-6965e21b2284_DATA_ECP_NETWORK_ADEQUACY.xlsm'
counties = 'Denver'
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
providers = providers[providers.County == counties]
# printing for sanity check
print(providers.head(10))
print(providers.info())
# Filter facilities by county(ies)
facilities = facilities[facilities.County == counties]
# printing for sanity check
print(facilities.head(10))
print(facilities.info())
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