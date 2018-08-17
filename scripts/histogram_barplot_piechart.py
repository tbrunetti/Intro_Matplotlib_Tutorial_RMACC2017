import matplotlib
matplotlib.use('Agg') 
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy
import pandas as pd
import collections

# bargraph/histogram example
# read in csv file, infers if header is available
data = pd.read_csv('/home/brunettt/matplotlib_tutorial_materials/datasets/GOT_battles.csv')
sns.countplot(x='year', data=data, palette='cubehelix')
sns.show()

# another bargraph/histogram examples

order_names=[]
most=collections.Counter(data['attacker_1']).most_common()
for tuples in most:
    order_names.append(tuples[0])
graph =sns.countplot(x='attacker_1', data=data, order=order_names)
for item in graph.get_xticklabels():
    item.set_rotation(45)
plt.set_title('Fight starter', fontsize=20)
plt.show()

'''
Take the original countplot of the year vs. total battles and reorder the x-axis to be in ascending order
'''

# pie chart using pandas
battle_locs = data['battle_type'].value_counts() # first count data, this is one disadvatage of pandas vs seaborn
battle_locs.plot.pie()

# fancier pie chart
battle_locs.plot(kind='pie', autopct='%.2f%%', explode=(0,0,0.2), startangle=180, shadow=True, colors=('#FFFF00', '#9900CC', '#99FF99'))
plt.title('Percentage of battle at specifed locations')
plt.ylabel('')
plt.axis('equal')
'''

'''
Try making a pie chart of the number of the percentage of wins of a battle when the attacker initiates
a battle.  Separte the pie piece from wins and losses, and choose your own color scheme.
'''