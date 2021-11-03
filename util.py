import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'

import math
from scipy.integrate import quad

"""
BSM Option Valuation
"""

### Helper Functions ###

def dN(x):
    '''Probability density function of standard normal random variable x'''
    return math.exp(-0.5 * x **2)/math.sqrt(2 * math.pi)

def N(d):
    '''Cumulative density function of standard normal random variable x'''
    return quad(lambda x: dN(x), -20, d, limit=50)[0]

def d1f(St, K, t, T, r, sigma):
    '''BSM d1 function.
    Parameters see e.g. BSM_call_value function'''
    d1 = (math.log(St / K) + (r + 0.5 * sigma ** 2)* (T-t)) / (sigma * math.sqrt (T-t))
    return d1

### Valuation Functions ###

def BSM_call_value(St, K, t, T, r, sigma):
    '''calculates BSM european call option value
    Parameters
    ===========
    St : stock/index level at time t
    K : strike price
    t : valuation date
    T : date of maturity / time to maturity if t =0; T>t
    r : constant, risk-less short rate
    sigma : volatility'''

    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T-t)
    call_value = St * N(d1) - math.exp(-r * (T-t)) * K * N(d2)
    return call_value

def BSM_put_value(St, K, t, T, r, sigma):
    put_value = BSM_call_value(St, K, t, T, r, sigma) - St + math.exp(-r * (T-t)) * K
    return put_value

### Plotting ###

def plot_values(function):
    plt.figure(figsize=(10, 8.3))
    points = 100

    #Model Parameters

    St = 100
    K = 100
    t = 0.0
    T = 1.0
    r = 0.05
    sigma = 0.2

    #C(K) plot
    plt.subplot(221)
    klist = np.linspace(80, 120, points)
    vlist = [function(St, K, t, T, r, sigma) for K in klist]
    plt.plot(klist, vlist)
    plt.grid()
    plt.xlabel('strike $K$')
    plt.ylabel('present value')

    #C(T) plot
    plt.subplot(222)
    tlist = np.linspace(0.0001, 1, points)
    vlist = [function(St, K, t, T, r, sigma) for T in tlist]
    plt.plot(tlist, vlist)
    plt.grid(True)
    plt.xlabel('Maturity $T$')

    #C(r) plot
    plt.subplot(223)
    rlist = np.linspace(0, 0.1, points)
    vlist = [function(St, K, t, T, r, sigma) for r in rlist]
    plt.plot(tlist, vlist)
    plt.grid(True)
    plt.xlabel('short rate $r$')
    plt.ylabel('present value')
    plt.axis('tight')

    #C(sigma) plot
    plt.subplot(224)
    slist = np.linspace(0.01, 0.5, points)
    vlist = [function(St, K, t, T, r, sigma) for sigma in slist]
    plt.plot(slist, vlist)
    plt.grid(True)
    plt.xlabel('Volatility $\sigma$')
    plt.tight_layout()
