### ROUGH DRAFT OF STUDY TIME PLOTS FOR D3 VISUALIZATION

# Explored 'my_pisa.csv' file created in 'clean_pisa.py' for relationships
# between student's confidence in math and other variables in the data.
# Number of observations: 480174
# Number of variables: 634

import pandas as pd 
import matplotlib.pyplot as plt

f = "my_pisa.csv"

#df = pd.read_csv(f)
df = pd.read_csv(f, skiprows=None, usecols=['ST42Q07', 'OUTHOURS', 'CNT'],
	dtype = {'ST42Q07': str, 'OUTHOURS': float, 'CNT': str})


head = df.head(n = 50)

#----------------------------------------------------------------------------------------------

### HOW DOES OUT OF SCHOOL STUDY TIME RELATE TO STUDENT'S CONFIDENCE IN MATH?

# Separate into groups based on study time(range 0.0 to 180.0).
# D3 viz will show low study time plot, then overlay moderate and high study 
# time plots on 'click'

# df of students with OUTHOURS <= 60
study_low_df = df[df['OUTHOURS'] <= 60.0]
low = study_low_df.groupby('ST42Q07').count()['CNT']
low_ratio = low / low.sum()
low_percent = low_ratio * 100
print low_percent


# Low Study Time Plot
fig = plt.figure() # Create matplotlib figure
ax = low_percent.plot(kind = 'bar', figsize=(10, 10), fontsize = 10, rot = 0)
fig.suptitle('Low Out of School Study Time', fontsize=15)
plt.xlabel('Math is one of my best subjects', fontsize=13)
plt.ylabel('Percentage of Students', fontsize=13)
#plt.show()

#---------------------------------------------------------------------------------------------

# df of students with OUTHOURS > 60 and <= 120
study_mid_df = df[(df['OUTHOURS'] > 60.0) & (df['OUTHOURS'] <= 120)]
mid = study_mid_df.groupby('ST42Q07').count()['CNT']
mid_ratio = mid / mid.sum()
mid_percent = mid_ratio * 100
print mid_percent

# Moderate Study Time Plot
fig = plt.figure() # Create matplotlib figure
ax = mid_percent.plot(kind = 'bar', figsize=(10, 10), fontsize = 10, rot = 0)
fig.suptitle('Moderate Out of School Study Time', fontsize=15)
plt.xlabel('Math is one of my best subjects', fontsize=13)
plt.ylabel('Percentage of Students', fontsize=13)
#plt.show()

#--------------------------------------------------------------------------------------------

# df of students with OUTHOURS > 120 and <= 180
study_high_df = df[(df['OUTHOURS'] > 120.0) & (df['OUTHOURS'] <= 180)]
high = study_high_df.groupby('ST42Q07').count()['CNT']
high_ratio = high / high.sum()
high_percent = high_ratio * 100
print high_percent

# High Study Time Plot
fig = plt.figure() # Create matplotlib figure
ax = high_percent.plot(kind = 'bar', figsize=(10, 10), fontsize = 10, rot = 0)
fig.suptitle('High Out of School Study Time', fontsize=15)
plt.xlabel('Math is one of my best subjects', fontsize=13)
plt.ylabel('Percentage of Students', fontsize=13)
#plt.show()

#-------------------------------------------------------------------------------------------

### CREATE NEW DATAFRAME AND WRITE TO CSV

# filename
f2 = 'pisa_viz.csv'

# create dataframe for 'response' column
response_df = pd.DataFrame(columns=['response'], data=['Agree', 'Disagree', 'Strongly agree', 'Strongly disagree'])

# reset index for these dataframes to avoid error during concatenation with response_df
low_percent.reset_index(drop=True, inplace=True)
mid_percent.reset_index(drop=True, inplace=True)
high_percent.reset_index(drop=True, inplace=True)

# Create new dataframe of concatenated dataframes
pisa_viz_df = pd.concat([pd.concat([response_df, low_percent, mid_percent, high_percent], axis=1)])

pisa_viz_df = pisa_viz_df.round(2)

# Change column names and write to csv file
pisa_viz_df.columns = ['response', 'low', 'mid', 'high']
pisa_viz_df.to_csv(f2, index = False)



