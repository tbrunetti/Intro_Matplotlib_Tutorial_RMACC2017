import matplotlib
matplotlib.use('Agg') 
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy
import pandas as pd

# grouped boxplot
stock_data = pd.read_table('all_stocks_1yr_modified.csv')
sns.boxplot(x="Month", y="Open", hue="Day", data=stock_data)

# grouped swarm plot
sns.swarmplot(x="Month", y="Open", data=stock_data, color='k')

# run together to overlay
sns.boxplot(x="Month", y="Open", data=stock_data)
sns.swarmplot(x="Month", y="Open", data=stock_data, color='k')


#boxplot using pandas -- generally easier to use than .plot(kind='bar')
stock_data.boxplot(column='Open', by='Month')



'''
TO DO:
Using pandas and seaborn load the data set dataset_Facebook.csv.  Although it ends in .csv, it is actually
demlimited by semicolons so please adjust accordingly.  Then create a boxplot where 
the category of 'Type' are the groups along your x-axis and your boxplots will represent
the number of people that that have liked the page AND engaged with the post and change
the font to be 2.0 in size.  Also, make the add the orient parameter and set it equal to 'h',
and set the notch parameter equal to True, and pick a color scheme of your choosing
'''
