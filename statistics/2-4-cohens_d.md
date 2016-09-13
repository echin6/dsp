[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import nsfg
import thinkstats2
import thinkplot
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohenD(group1, group2):
    diff = group1.mean() - group2.mean()
    
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    
    d = diff /  math.sqrt(pooled_var)
    return d

first_wgt_hist = thinkstats2.Hist(firsts.totalwgt_lb)
other_wgt_hist = thinkstats2.Hist(others.totalwgt_lb)

width = 0.05
thinkplot.PrePlot(2)
thinkplot.Hist(first_wgt_hist, align='right', width=width)
thinkplot.Hist(other_wgt_hist, align='left', width=width)
thinkplot.Show(xlabel='lbs', ylabel='frequency')

firsts.totalwgt_lb.mean
others.totalwgt_lb.mean

prglngth_CohenD = CohenD(firsts.prglngth, others.prglngth)
totalwgt_lb_CohenD = CohenD(firsts.totalwgt_lb, others.totalwgt_lb)

prglngth_CohenD
totalwgt_lb_CohenD

#To understand if the difference in means of the birth weights is significant between the firstborns and others, we first look the distribution visually.  Both groups exhibit normal distribution with the mean weight centering around 7-8lbs.  The mean weight of the firstborns is 8.8lbs, while the mean weight of the others is 7.9lbs.  At first glance this would suggest there could be a difference in weight with statistical signficance.  However, when we compute the Cohen's d statistics, we get -0.089.  Similar to the Cohen's d of 0.029 we computed for pregnancy length, this would suggest the difference in means is small and insignificant.  The difference in means we observed is merely a result of randomness and sample size difference.
