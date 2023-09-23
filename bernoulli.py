'''
Bernoulli distribution : 
 most basic of discrete probability distributions, 
 2 possible outcomes -> SUCCESS OR FAILURE 


Ber(p) with 0 <= p <= 1 


lets take a simple example : 



'''

import numpy as np 


def bernoulli_trials(n,p):
    #initialize number of success 
    nbrSuccesses = 0

    if (p<0) or (p>1):
        raise ValueError("Probability p must be between 0 and 1.")
    
    #perform trials 
    for i in range(n):
        #choose random number between 0 and 1 
        random_number = np.random.random()
         #if less than p then success 
        if random_number < p:
            nbrSuccesses += 1
   
    return nbrSuccesses


#lets test this 
bersample = bernoulli_trials(1,0.3)

print(bersample)




    




