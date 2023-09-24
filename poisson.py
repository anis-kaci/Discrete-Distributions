'''

    Poisson distribution : 
      models the occurence of an event , over time 
      ex : if someone trains 3 times a week , whats the proba he will
      train 4 times

      p(X=k) = (lambda^k)/k! * exp(-lambda)

      k will be four and lambda 3 here for example 



'''

import numpy as np 

#we can also use scipy 
from scipy.stats import poisson

def poissonBrute(lam,k):
    return ((lam**k)/np.math.factorial(k)) * np.exp(-lam)



#lets test it 
poissonProba = poissonBrute(3,4)

print(poissonProba)


def poissonScypi(lam,k):
    return poisson.pmf(k, lam)


print(poissonScypi(3,4))




