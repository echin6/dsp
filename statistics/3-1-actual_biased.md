[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Read the female respondent file.  

%matplotlib inline  

import chap01soln  
resp = chap01soln.ReadFemResp()  

#Make a PMF of numkdhh, the number of children under 18 in the respondent's household.  

import thinkstats2  
numc18 = resp.numkdhh  
pmf = thinkstats2.Pmf(numc18, label="Actual")  

#Display the PMF.  

import thinkplot  
thinkplot.Pmf(pmf)  
thinkplot.Show(xlabel='No. of children under 18', ylabel='PMF')  

#Define <tt>BiasPmf</tt>.  

def BiasPmf(pmf, label=''):  
    """Returns the Pmf with oversampling proportional to value.  
​
    If pmf is the distribution of true values, the result is the  
    distribution that would be seen if values are oversampled in  
    proportion to their values; for example, if you ask students  
    how big their classes are, large classes are oversampled in  
    proportion to their size.  
​
    Args:  
      pmf: Pmf object.  
      label: string label for the new Pmf.  
​
     Returns:  
       Pmf object  
    """
    new_pmf = pmf.Copy(label=label)  
​
    for x, p in pmf.Items():  
        new_pmf.Mult(x, x)  
        
    new_pmf.Normalize()  
    return new_pmf  

#Make a the biased Pmf of children in the household, as observed if you surveyed the children instead of the respondents.

biased_pmf = BiasPmf(pmf, label="Surveyed")  

#Display the actual Pmf and the biased Pmf on the same axes.  

thinkplot.PrePlot(2)  
thinkplot.Pmfs([pmf, biased_pmf])  
thinkplot.Show(xlabel="No. of Children under 18", ylabel="PMF")   

#Compute the means of the two Pmfs.  

print("Actual Mean", pmf.Mean())  

#('Actual Mean', 1.0242051550438309)  

print("Surveyed Mean", biased_pmf.Mean())  

#('Surveyed Mean', 2.4036791006642821)  
