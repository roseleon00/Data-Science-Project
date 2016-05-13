# Rosanna De Leon R.

# Data Science

# Final Project



#show the percentage of New York city's aparment prices in each borough
#view-source:http://streeteasy.com/for-rent/manhattan/beds:2?view=map#pos=12/40.75974,-73.94932

import matplotlib.pyplot as plt
import numpy as np

manhattan = [2195,6095,9495, 5000, 2650,7200,6000,8500,10000,5595,2000,3980,8000,2933,9500,6000,2395,1700,1990, 4200]
brooklyn =  [1800,2750,1400, 1050, 2495,1800,2700,3995,1995,3000,2130,2500,2999,2100,2500,2999,2100,2495,1800, 2700]
queens =    [3995,2900,2100, 2650, 2000,2500,3195,2000,2495,2300,2200,2300,2495,1900,3500,3000,2100,2650,2000, 2500]
bronx =     [3900,1950,1699, 1750, 1699,1475,1995,1300,2195,2349,1750,1885,1350,1050,1795,1840,1995,1850,1450, 1950]
staten_is = [2925,3995,1200, 2200, 2200,2100,1910,2600,3500,3000,3700,4200,2825,3000,2550,3200,3100,4000,2700, 2200]

total =     [14815,17690,15894,12650,11044,15075,15800,15795,20185,16244,11780,14865,17669,10953,19845,17039,11690,12695,9940,13550]
ids =       [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

percentage = []

for i in range(len(manhattan)):
	percentage.append(manhattan[i]*100/float(total[i]))
plt.plot(ids, percentage, color='g', label="Manhattan")

percentage = []

for i in range(len(brooklyn)):
	percentage.append(brooklyn[i]*100/float(total[i]))
plt.plot(ids, percentage, color='r', label="Brooklyn")

percentage = []

for i in range(len(queens)):
	percentage.append(queens[i]*100/float(total[i]))
plt.plot(ids, percentage, color='b', label="Queens")

percentage = []

for i in range(len(bronx)):
	percentage.append(bronx[i]*100/float(total[i]))
plt.plot(ids, percentage, color='y', label="Bronx")

percentage = []

for i in range(len(staten_is)):
	percentage.append(staten_is[i]*100/float(total[i]))
plt.plot(ids, percentage, color='purple', label="Staten Island")

print "Manhattan: " , np.average(manhattan)
print "Brooklyn: " , np.average(brooklyn)
print "Queens: " , np.average(queens)
print "Bronx: " , np.average(bronx)
print "Staten Island: " , np.average(staten_is)


plt.title("Apartment Prices \nPercentage of New York City Apartment Prices")#Title for plot
plt.xlabel('ID Apartments')                #Label for x-axi
plt.ylabel('Percentage')                   #Label for the y-axis
plt.legend(loc = 1,fontsize = 'small')#Make a legend in upper left corner
plt.show()