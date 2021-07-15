import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


def markov_move( trans, start ) :
    myrand, myvar, accum  = np.random.uniform(0,1), 0, trans[start,0]
    while myrand>accum :
          myvar = myvar + 1
          accum = accum + trans[start,myvar]
    return myvar

def is_transition( trans, start, nsteps, target ) :
    for i in range(nsteps) : start = markov_move( trans, start )
    if start==target : return 1
    return 0

def sample_mean( trans, start, nsteps, target, nsamples ) :
    mean = 0
    for i in range(nsamples) : mean = mean + is_transition( trans, start, nsteps, target )
    mean = mean / nsamples 
    var = mean*(1-mean)
    conf = np.sqrt( var / nsamples )*scipy.stats.norm.ppf(0.95)
    return mean, conf

# Setup the transition matrix here
A = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])


# Now estimate some hitting probablities if we start from state 2
for i in range(3) :
    for j in range(3) : 
        prob, conf = sample_mean( A, i, 10, j, 100 )
        print("There is a 90% probablity that element", i+1, j+1, "of the 10-step transition probablity matrix is within", conf, "of", prob )
