### CLEAN PISA DATA:
### Choose variables to include, then clean all values for chosen variables
### and write cleaned data to a new csv.

import pandas as pd

### READ CSV INTO PANDAS DATAFRAME
 
# The data to load
f = "pisa2012.csv"

# Read the csv data, specify data types columns
pisa_df = pd.read_csv(f, skiprows=None, usecols=['CNT', 'COBN_S', 'AGE', 'EXAPPLM', 'EXPUREM', \
	'BELONG', 'ST04Q01', 'ST11Q01', 'ST11Q02', 'ST11Q03', 'ST11Q04', 'ST13Q01', 'ST15Q01', \
	'ST17Q01', 'ST19Q01', 'ST26Q02', 'ST26Q06', 'ST26Q07', 'ST26Q08', 'ST26Q09', 'ST42Q01', \
	'ST42Q08', 'ST42Q07', 'ST43Q06', 'ST87Q05', 'IC01Q02', 'IC01Q07', 'OUTHOURS', 'PARED', \
	'TIMEINT'], \
	dtype = {'CNT': str, 'COBN_S': str, 'AGE': float, 'EXAPPLM': float, 'EXPUREM': float, \
	'BELONG': float, 'ST04Q01': str, 'ST11Q01': str, 'ST11Q02': str, 'ST11Q03': str, \
	'ST11Q04': str, 'ST13Q01': str, 'ST15Q01': str, 'ST17Q01': str, 'ST19Q01': str, \
	'ST26Q02': str, 'ST26Q06': str, 'ST26Q07': str, 'ST26Q08': str, 'ST26Q09': str, \
	'ST42Q01': str, 'ST42Q08': str, 'ST42Q07': str, 'ST43Q06': str, 'ST87Q05': str, \
	'IC01Q02': str, 'IC01Q07': str, 'OUTHOURS': float, 'PARED': float, 'TIMEINT': float})

head = pisa_df.head(n=50)

#-----------------------------------------------------------------------------------------------

### CLEAN ISCED EDUCATION VALUES

def ISCED(level):

	# nan values were cast as type float, converted to string
	if type(level) == float:
		level = str(level)

	if '3A' in level:
		level = 'level 3A'

	elif '3B' in level:
		level = 'level 3B 3C'

	elif '2' in level:
		level = 'level 2'

	elif '1' in level:
		if 'She' in level:
			level = 'Did not complete level 1'
		else:
			level = 'level 1'

	else:
		level = None

	return level


# take in one column from dataframe and apply conversion to all isced levels. 
def all_ISCED(levels):
	return levels.map(ISCED)

# set old isced column equal to cleaned isced column
pisa_df.loc[:,('ST13Q01')] = all_ISCED(pisa_df.loc[:,('ST13Q01')])
pisa_df.loc[:,('ST17Q01')] = all_ISCED(pisa_df.loc[:,('ST17Q01')])

#-----------------------------------------------------------------------------------------------

### CLEAN EMPLOYMENT VALUES

def employment(status):

	# nan values were cast as type float, converted to string
	if type(status) == float:
		status = str(status)

	if 'full' in status:
		status = 'FULL'

	elif 'part' in status:
		status = 'PART'

	elif 'Not' in status:
		status = 'UNEMPLOYED'

	elif 'Other' in status:
		status = 'OTHER'

	else:
		status = 'NONE'

	return status 



def all_employment(statuses):
	return statuses.map(employment)

pisa_df.loc[:,('ST15Q01')] = all_employment(pisa_df.loc[:,('ST15Q01')])
pisa_df.loc[:,('ST19Q01')] = all_employment(pisa_df.loc[:,('ST19Q01')])

#------------------------------------------------------------------------------------------------

### WRITE TO CSV FILE

f = "my_pisa.csv"
pisa_df.to_csv(f, index = False)

#print head


