import matplotlib.pyplot as plt 
import numpy as np 

def binomial( n, p ) : 
  # Your code to generate the binomial random variable Y goes here
  

def gen_x(n, p ) : 
  # Your code to generate samples of the random vairable X goes here
  # this function should include a call to binomial.
  

# You should not need to adjust any of the code from here onwards.
# This code simply generates some samples from the distribution of X 
# and plots them
xvals, samples = np.zeros(100), np.zeros(100) 
for i in range(100) : xvals[i], samples[i] = i+1, gen_x( 10, 0.4 )
plt.plot( xvals, samples, 'ko' )
plt.savefig("xvals.png")
