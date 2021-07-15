try:
    from AutoFeedback.funcchecks import check_func
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

from AutoFeedback.randomclass import randomvar
import unittest
from main import *

myp = np.array([[0.3,0.5,0.2],[0.3,0.4,0.3],[0.2,0.5,0.3]])

class helper : 
   def test_mean( probs, start, steps, end, n ) :
       m, e = sample_mean( probs, start, steps, end, n )
       return m
 
   def test_var( probs, start, steps, end, n ) :
       m, e = sample_mean( probs, start, steps, end, n )
       return ( e / scipy.stats.norm.ppf(0.95) )**2 

class UnitTests(unittest.TestCase) :
   def test_markov_move(self) :      
       myvars, inputs, variables = np.array([0,1,2]), [], [] 
       for j in range(5) : 
           exp = np.dot( myp[j,:], myvars )
           var = var = np.dot( myp[j,:], myvars*myvars ) - exp*exp
           for i in range(10):
               inputs.append((myp,j,))
               myvar = randomvar( exp, variance=var, vmin=0, vmax=2, isinteger=True )
               variables.append( myvar )

       assert( check_func("markov_move", inputs, variables ) )

   def test_endstate(self) :
       inputs, variables = [], [] 
       for i in range(2,12) :
           myprobs = np.linalg.matrix_power( myp, i )
           for s in range(3) :
               for e in range(3) : 
                   inputs.append((myp,s,i,e,))
                   p = myprobs[s,e]
                   myvar = randomvar( p, variance=p*(1-p), vmin=0, vmax=1, isinteger=True )
                   variables.append( myvar )
       assert( check_func("is_transition", inputs, variables, calls=["markov_move"] ) )

   def test_mean(self) :
       ns, inputs, variables = 100, [], []
       for i in range(2,4) :
           nsteps = i*10
           myprobs = np.linalg.matrix_power( myp, nsteps )
           for s in range(3) :
               for e in range(3) :
                   inputs.append((myp,s,nsteps,e,ns,))
                   p = myprobs[j-1,1]
                   myvar = randomvar( p, variance=p*(1-p)/ns, vmin=0, vmax=1, isinteger=False )
                   variables.append( myvar )
       assert( check_func("test_mean", inputs, variables, modname=helper ) )

   def test_var(self) :
       ns, inputs, variables = 100, [], []
       for i in range(2,4) :
           nsteps = i*10
           myprobs = np.linalg.matrix_power( myp, nsteps )
           for s in range(3) :
               for e in range(3) :
                   inputs.append((myp,s,nsteps,e,ns,))
                   p = myprobs[j-1,1]
                   myvar = randomvar( p, dist="chi2", variance=p*(1-p)/ns, isinteger=False )
                   variables.append( myvar )
       assert( check_func("test_var", inputs, variables, modname=helper ) )
