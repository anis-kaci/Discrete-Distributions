'''

  Geometric distribution :
    keep trying till we get a success after X number of bernoulli trials 

    so X : proba that an event will take X bernoulli trials to happen 



'''

import numpy as np 

def geom(p):
    x = 1

    if (p<0) or (p>1):
        raise ValueError ('Probability must be between 0 and 1')

    while(True):
        #generate a random number 
        random_number = np.random.random()
    
        if random_number < p :
            return x
        else:
            x += 1



#lets test this with a free throws example (basketball)
#lets say a player has 30% chance of getting a perfect free throw

shotsBeforePerfectShot = geom(0.3)

print(str(shotsBeforePerfectShot) + ' Fts before perfect one')






    

