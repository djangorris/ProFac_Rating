import pandas as pd

def cigna_workaround(file,ext_removed,carrier_var,carrier_name,unique_providers,unique_facilities):
	providers1 = pd.read_excel(file,
		            sheetname='IndividualProviders1',
		            header=1,
		            parse_cols = [0,12],
		            )
	# Parse all facilities and pharmacies
	facilities1 = pd.read_excel(file,
		            sheetname='Facilities&Pharmacies1',
		            header=1,
		            parse_cols = [0,7],
		            )
	providers1.columns = ['NPI','County']
	facilities1.columns = ['NPI','County']
	# Count unique providers
	unique_providers1 = providers1.NPI.nunique()
	# Count unique facilities and pharmacies
	unique_facilities1 = facilities1.NPI.nunique()
	providers2 = pd.read_excel(file,
		            sheetname='IndividualProviders2',
		            header=1,
		            parse_cols = [0,12],
		            )
	# Parse all facilities and pharmacies
	facilities2 = pd.read_excel(file,
		            sheetname='Facilities&Pharmacies2',
		            header=1,
		            parse_cols = [0,7],
		            )
	providers2.columns = ['NPI','County']
	facilities2.columns = ['NPI','County']
	# Count unique providers
	unique_providers2 = providers2.NPI.nunique()
	# Count unique facilities and pharmacies
	unique_facilities2 = facilities2.NPI.nunique()
	# Sum unique1 and unique2
	unique_providers = unique_providers1 + unique_providers2
	unique_facilities = unique_facilities1 + unique_facilities2
	return unique_providers, unique_facilities