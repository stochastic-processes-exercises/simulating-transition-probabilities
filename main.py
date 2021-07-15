import matplotlib.pyplot as plt
import scipy.stats
import numpy as np


def markov_move( trans, start ) :


def is_transition( trans, start, nsteps, target ) :


def sample_mean( trans, start, nsteps, target, nsamples ) :

    return mean, conf

# Setup the transition matrix here
A = 


# Now estimate some hitting probablities if we start from state 2
for i in range(3) :
    for j in range(3) : 
        prob, conf = sample_mean( A, i, 10, j, 100 )
        print("There is a 90% probablity that element", i+1, j+1, "of the 10-step transition probablity matrix is within", conf, "of", prob )
