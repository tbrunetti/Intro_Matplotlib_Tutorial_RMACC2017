import matplotlib
matplotlib.use('Agg') 
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy
import pandas as pd

# jointplots with Pearson's correlation, p-value and confidence intervals
facebook = pd.read_csv('dataset_Facebook.csv', sep=';')
sns.jointplot('Total Interactions', 'comment', data=facebook, kind='reg', color='g', size=10)
sns.jointplot('Total Interactions', 'comment', data=facebook, kind='kde', color='g', size=10)
sns.jointplot('Total Interactions', 'comment', data=facebook, kind='hex', color='g', size=10)

sns.jointplot('Total Interactions', 'comment', data=facebook, kind='reg', color='orange', size=10, xlim=(-50, 1000), ylim=(-20, 50))
sns.jointplot('Total Interactions', 'comment', data=facebook, kind='kde', color='orange', size=10, xlim=(-50, 1000), ylim=(-20, 50))
sns.jointplot('Total Interactions', 'comment', data=facebook, kind='hex', color='orange', size=10, xlim=(-50, 1000), ylim=(-20, 50))



# scatter plot based on size; data with more than 2 dimensions
age = [5, 6, 7, 8, 9, 10, 11, 12]
avg_continuous_sleep = [5, 5, 7, 6.5, 8, 6.5, 7, 8]
total_participants = [1000, 900, 200, 230, 670, 420, 900, 150]
colors = np.random.rand(len(age))

plt.scatter(age, avg_continuous_sleep, s=total_participants, c=colors, alpha=0.50)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.xlabel('age (years)', fontsize=15)
plt.ylabel('average hours of continuous sleep', fontsize=15)
plt.title('average contnuous sleep within each age group', fontsize=15)
plt.show()