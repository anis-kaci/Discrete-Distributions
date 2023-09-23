'''

  binomial is n ber(p) trials 
  
  so we ll use the same function we used in bernoulli 

  
'''

import numpy as np

def bin(n,p): 
    if (p<0) or (p>1): 
        raise ValueError('Probability must be between 0 and 1')
    
    numberofS = 0 

    #init results array 
    results = []

    for i in range(n):
        randomNum = np.random.random() 
        if randomNum < p :
            numberofS += 1
            outcome = 'S'
        else:  
            outcome = 'F'

    
     #print results of the trials in an array 
        results.append(outcome)
    
    return results

    #or return results , numberofS



#Tests 

TestRes = bin(30, 0.43)

#or TestRes, successes = bin(30, 0.43)

print(TestRes)

