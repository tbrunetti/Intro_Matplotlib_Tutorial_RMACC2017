import matplotlib
#matplotlib.use('Agg') 
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy
import pandas as pd

def main():
	# make a very basic scatter plot
	plt.plot([1, 2, 3, 4, 5, 6, 7], [30, 20, 10, 0, 10, 20, 30], 'ro')
	plt.xlabel('time')
	plt.ylabel('speed (mph)')
	plt.title('ball speed over time')
	plt.show()

	# multiple trials plots
	time_points = np.arange(0, 10, 1)
	response_1 = [0, .2, .4, .8, 1.6, 3.2, 3.2, 3.2, 3.2, 3.2]
	response_2 = [0, .1, .2, .4, .8, 1.6, 3.2, 6.4, 12, 12]
	response_3 = [0, .1, .2, .3, .4, .8, 1.6, 1.6, 1.6,  1.6]
	plt.plot(time_points, response_1, 'g*', label='trial1')
	plt.plot(time_points, response_2, 'rH', label='trial2')
	plt.plot(time_points, response_3, 'bv', label='trial3')
	plt.ylabel('response')
	plt.xlabel('time (min)')
	plt.title('Drug response over time')
	plt.legend(loc='upper left')
	plt.show()


'''
try running line 17-28 above except replace response_1 'g*' to 'g-', response_2 'rH' tp 'r-', 
 and response_3 to 'b-'; repeat this excersize now changing 'g-' to 'g--' and 'r-' to 'r--', and 'b-' to 'b--'
'''
if __name__=='__main__':
	main();