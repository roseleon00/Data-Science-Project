'''
    Yelso Yanez
        and
    Rossana de Leon

    Data Science Group project 

'''

import matplotlib.pyplot as plt
import csv

years = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

with open('NYPD_7_Major_Felony_Incident_Map.csv') as f:
    reader = csv.reader(f)
    reader.next()
    #since we want to keep track of how many felonies occured each year, we will have 
    
    Bcount = 0
    Mcount = 0
    Scount = 0
    BKcount = 0
    Qcount = 0
    
#############################################    
 #since we also wanna keep track of how many felonies are occuring year to year in each borough, we use lists to store those values:
    #This empty list starts off at the year 2005 and continues on to 2015
##    #2005....2009........2015
    ByearCount= [0,0,0,0,0,0,0,0,0,0,0]                                   
    MyearCount = [0,0,0,0,0,0,0,0,0,0,0]
    SyearCount = [0,0,0,0,0,0,0,0,0,0,0]
    BKyearCount = [0,0,0,0,0,0,0,0,0,0,0]
    QyearCount = [0,0,0,0,0,0,0,0,0,0,0]
##

with open('NYPD_7_Major_Felony_Incident_Map.csv') as f:
    reader = csv.reader(f)
    reader.next()

###to make better the program remove the bcount because the list of byearcount can be add so can show 
### be show in the simple bar graph
###try to make the program more dynamic, try to modify the program so can show year or individual sections
###This is for testing. we can remove later

    for row in reader:
        try:
            if int(row[6])>2004:
                if row[12] == "FELONY":# and int(row[6]) > 2004:
                    if row[15] == "BRONX":
                        Bcount += 1
                        ByearCount[2015-int(row[6])]+=1
                    elif row[15] == "MANHATTAN":
                        Mcount += 1
                        MyearCount[2015-int(row[6])]+=1
                    elif row[15] == "STATEN ISLAND":
                        Scount += 1
                        SyearCount[2015-int(row[6])]+=1
                    elif row[15] == "BROOKLYN":
                        BKcount += 1
                        BKyearCount[2015-int(row[6])]+=1
                    elif row[15] == "QUEENS":
                        Qcount += 1
                        QyearCount[2015-int(row[6])]+=1
                    else:
                        pass
        except:
            ValueError
##            print "f u python"
            pass
        ByearCount.reverse()
        MyearCount.reverse()
        SyearCount.reverse()
        BKyearCount.reverse()
        QyearCount.reverse()

my_xticks = ['Bronx','Manhattan','Staten Island','Brooklyn','Queens']
plt.xticks([1.4,2.4,3.4,4.4,5.4],my_xticks)
barlist = plt.bar([1,2,3,4,5],[Bcount,Mcount,Scount,BKcount,Qcount])
barlist[0].set_color('r')
barlist[1].set_color('g')
barlist[2].set_color('b')
barlist[3].set_color('y')
barlist[4].set_color('b')
plt.title("Felony in NYC for the last 10 years")
plt.xlabel("Total felony by borough")
plt.ylabel("Amount of felony for last 10 years")
plt.show()

plt.plot(years,ByearCount, label = 'Bronx')
plt.plot(years,MyearCount, label = 'Manhattan')
plt.plot(years,SyearCount, label = 'Staten Island')
plt.plot(years,BKyearCount, label = 'Brooklyn')
plt.plot(years,QyearCount, label = 'Queens')
plt.ylabel("Total amoung of Felony by NYC borough")
plt.xlabel("Felony from 2005 to 2015")
plt.legend()
plt.show()