import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_genx(self) : 
        for n in range(10,15) : 
           for p in [0.2,0.4,0.6] : 
               mean = 0 
               for k in range(100) : mean = mean + gen_x(n,p) 
               var = (n-1)*n*p*p 
               bar = np.sqrt(var/100)*scipy.stats.norm.ppf( (0.99+1)/2)
               estmean = n*p*(( 1-p)**n + p - 1 ) / (p-1)
               self.assertTrue( np.abs( mean/100 - estmean) < bar )
