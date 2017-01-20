# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:38:01 2016

@author: xc
"""


import pylab as pl
#最小支持度15
#x1 = [10000, 50000, 100000, 200000, 300000, 400000, 500000, 1000000]# Make an array of x values
#y1 = [4.11,  18.24, 35.9,   73.27,  107.30, 144.02, 180.95, 400.36]# Make an array of y values for each x value
#pl.xlabel('Number of record')
#pl.ylabel('Time')
#pl.plot(x1, y1,'ob-')# use pylab to plot x and y

#最小支持度500
x2 = [10000, 50000, 100000, 200000, 300000, 400000, 500000, 1000000]
y2 = [1.78,  13.37, 26.56,  52.83,  79.57,  104.95, 131.38, 443.29 ]
pl.xlabel('Number of record')
pl.ylabel('Time')
pl.title('minsupport = 500')
pl.plot(x2, y2,'sg-')# use pylab to plot x and y

#最小支持度10000
#x2 = [10000, 50000, 100000, 200000, 300000, 400000, 500000, 1000000]
#y2 = [0.25,  4.04,  14.25,  41.56 , 62.19,  96.91,  120.07, 354.37 ]
#pl.xlabel('Number of record')
#pl.ylabel('Time')
#pl.plot(x2, y2,'xr-')# use pylab to plot x and y

#20w记录
x3 = [   500,   1000,  5000,  10000, 50000, 100000]
y3 = [   57.15, 52.64, 48.64, 40.52, 8.73, 4.33]
pl.xlabel('minsupport')
pl.ylabel('Time')
pl.title('record = 20W ')
pl.plot(x3, y3,'ok-')# use pylab to plot x and y

pl.show()# show the plot on the screen