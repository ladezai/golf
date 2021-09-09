from itertools import count
from math import gcd

"""
    A fast and short fibonacci numbers
    generator. 
    See https://oeis.org/A000045
"""

def fib(i,j):yield i;yield from f(j,i+j)

"""
    A compact prime generator.
    See https://oeis.org/A000040.

"""
def primes(x,s):y=next(filter(lambda i:all([i%k for k in s]),range(x,2*x)));yield y;yield from p(y,s+[y])

"""
    The squares generator.
    See https://oeis.org/A000290
"""
def psq(x):yield from (y*y for y in count(x,1))

"""
    Triangular numbers generator.
    See https://oeis.org/A000217 
"""
def tri(x): yield from (y*(y+1)//2 for y in count(x,1))

"""
    Euler totient generator.
    See https://oeis.org/A000010
"""
def ephi(x): yield from (sum(gcd(k,y)==1 for k in range(y)) for y in count(x,1))
