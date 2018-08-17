import matplotlib
matplotlib.use('Agg') 
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy
import pandas as pd

# read in and re-order the dataframe
eur_qol = pd.read_csv('european_quality_of_life.csv') # look at dataframe structure
order = eur_qol.pivot('Country', 'Gender', 'Mean') # order re-organizes dataframe
sns.clustermap(order) # most basic
sns.heatmap(order) # most basic


# pretty heatmap
sns.set(font_scale = 1.0)
sns.heatmap(order, linewidths=0.25, cmap='Blues', square=True)  

# annotated heatmap
sns.set(font_scale = 1.0)
sns.heatmap(order, annot=True, fmt= 'f', linewidths=0.50, cmap='BrBG')

# customized clustermap
sns.set(font_scale = 1.0)
sns.clustermap(order, linewidths=0.25, cmap='coolwarm', method = 'centroid', metric = 'hamming')

'''
make a heatmap by loading in the data called GSE27233_GEO_subset.txt and use a diverging color map
'''