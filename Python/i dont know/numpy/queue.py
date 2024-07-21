import numpy as np
import math as m
import matplotlib.pyplot as plt
import random

def poisson(x, mu):
    p = np.exp(-mu) * mu**x / m.factorial(x)
    return p

def exponential(x, lam):
    e = lam * np.exp(-lam * x)
    return e

lam = np.random.randint(1, 15) # arrival rate
mu = np.random.randint(1, 15) # service rate
s = np.random.randint(1, 15) # number of servers
n = np.random.randint(1, 15) # number of customers
print('lam: \n', lam)
print('mu: \n', mu)
print('s: \n', s)
print('n: \n', n)

rho = lam / (s * mu)
print('rho: \n', rho)

if rho == 0 or rho > 1: 
    print('give up')
else:
    '''pi_0'''
    def pmf_insystem(rho, s):
        sum1 = sum([(s * rho)**i / m.factorial(i) for i in range(s)])
        oth = ((s * rho)**s / (m.factorial(s)) * (1 / (1 - rho)))
        p = 1 / (sum1 + oth)
        return p
    p0 = pmf_insystem(rho, s)
    print('p0: \n', p0)

    '''pi_k'''
    def pmf_iterative(rho, n):
        # for i in range(n):
                if lam>mu: 
                    p_n= p0*(s*rho)**n / m.factorial(n)   
                else:
                    p_n= p0*(((((s*rho)**n)*n**(s-n)))/m.factorial(s)) 
                return p_n      
    nth = pmf_iterative(rho, s)
    print('nth: \n',nth)

    '''number of customers in the system'''
    def in_sys(s, rho):
        sum1 = sum([(s * rho)**i / m.factorial(i) for i in range(s-1)])
        c = 1 / (1 + (1 - rho) * (m.factorial(s) * sum1))
        waiting = ((rho / (1 - rho)) * c) + s * rho
        return waiting
    wait = in_sys(s, rho)
    print('wait: \n', wait)

    '''Response time'''
    def response(s, rho):
        sum1 = sum([(s * rho)**i / m.factorial(i) for i in range(s-1)])
        c = 1 / (1 + (1 - rho) * (m.factorial(s) * sum1))
        r = (c/((s*mu)-lam))+(1/mu)
        return r
    response = response(s, rho)
    print('response: \n',response)

    sum1 = sum([(s * rho)**i / m.factorial(i) for i in range(s-1)])
    c = 1 / (1 + (1 - rho) * (m.factorial(s) * sum1))
    print('c: \n', c)
    
time = 1000
t = 0
n = 0
t_avgpop = 0

while True:
    po = lam + mu * n
    step = random.expovariate(po)
    t += step
    t_avgpop += n*step
     
    if t>= time:
        break
    
    if random.uniform(0,po) < lam:
        n+= 1
    else:
        n-= 1
        
avg = t_avgpop/time
print('idk tbh', (avg - rho)/rho * 100)






