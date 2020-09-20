from random import random 
from numpy import zeros 


def power_law_cdf(x ,x0, alpha):
    return 1 - (x0/x)**(alpha-1)

def power_law_pdf(x ,x0, alpha):
    return (alpha-1.)*x0**(alpha-1.)*1./x**alpha

def power_law_rngen(x0,alpha):
    y = random()
    return x0/(1-y)**(1./(alpha-1.))

def power_law_with_init_plateau_cdf(xvals ,x0, alpha):
    cdf = zeros(len(xvals), float)
    for i,x in enumerate(xvals):
        if x > x0:
            cdf[i] = (alpha-1)/alpha + (1 - (x0/x)**(alpha-1))/alpha
        elif x >= 0:
            cdf[i] = (alpha-1)/alpha*x/x0
        else:
            cdf[i] = 0.
    return cdf

def power_law_with_init_plateau_pdf(xvals ,x0, alpha):
    pdf = zeros(len(xvals), float)
    for i,x in enumerate(xvals):
        if x > x0:
            pdf[i]= (alpha-1)/alpha * x0**(alpha-1.)*1./x**alpha
        elif x >= 0.:
            pdf[i]= (alpha-1)/alpha/x0
        else: 
            pdf[i] = 0.
            
    return pdf

def power_law_with_init_plateau_rngen(x0,alpha):
    y = random()
    if y < (alpha-1.)/alpha:
        return alpha*1./(alpha-1.)*x0*y
    else:
        return x0/(alpha*(1-y))**(1./(alpha-1))
