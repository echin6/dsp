[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

import numpy as np  
import random  
import thinkstats2  
import thinkplot  
%matplotlib inline  
import matplotlib.pyplot as plt  

y = []  
for x in range(0,1000):  
    y.append(np.random.random())  

pmf = thinkstats2.Pmf(y, label="1000 rnd numbers")  
thinkplot.Pmf(pmf, linewidth = 0.1)  
thinkplot.Show()  

cdf = thinkstats2.Cdf(y, label="1000 rnd numbers")  
thinkplot.Cdf(cdf)  
thinkplot.Show(xlabel="numbers", ylabel='CDF')  

# Distribution looks unifrom based on the CDF graph  
