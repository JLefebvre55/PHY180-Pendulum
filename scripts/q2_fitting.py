filename="../data/q2_data.txt"
# change this if your filename is different

import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt

data=loadtxt(filename, usecols=(0,1,2,3), skiprows=1, unpack=True)
# load filename, take columns 0 & 1 & 2 & 3, skip 1 row, unpack=transpose x&y
b = 1500
a = 1000
xdata=np.array(data[0][a:b])
ydata=np.array(data[1][a:b])
xerror=np.array(data[2][a:b])
yerror=np.array(data[3][a:b])
# finished importing data, naming it sensibly

def my_func(theta,a,tau,T,phi):
    return a*np.exp(-theta/tau)*np.cos(2*np.pi*theta/T+phi)

# this is the function we want to fit. the first variable must be the
# x-data (time), the rest are the unknown constants we want to determine

popt, pcov = optimize.curve_fit(my_func, xdata, ydata, [0.88, 100, 2, 0, 0])
# we have the best fit values in popt[], while pcov[] tells us the uncertainties

a=popt[0]
tau=popt[1]
T=popt[2]
phi=popt[3]
# best fit values are named nicely
u_a=pcov[0,0]**(0.5)
u_tau=pcov[1,1]**(0.5)
u_T=pcov[2,2]**(0.5)
u_phi=pcov[3,3]**(0.5)
# uncertainties of fit are named nicely

def fitfunction(t):  
    return a*np.exp(-t/tau)*np.cos(2*np.pi*t/T+phi)
#fitfunction(t) gives you your ideal fitted function, i.e. the line of best fit

start=min(xdata)
stop=max(xdata)    
print(start, stop)
xs=np.arange(start,stop,xdata[1]-xdata[0]) # fit line has 1000 points
curve=fitfunction(xs)
# (xs,curve) is the line of best fit for the data in (xdata,ydata) 

plt.rcParams["figure.figsize"] = (10,6)
# Change the size of your plot - numbers are inches because USA

plt.errorbar(xdata,ydata,yerr=yerror,xerr=xerror,fmt=".")
# plot the data, fmt makes it data points not a line
plt.plot(xs,curve)
# plot the best fit curve on top of the data points as a line

plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (rad)")
plt.title("Best Fit of Pendulum Amplitude over Time")
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph


print("A:", a, "+/-", u_a)
print("tau:", tau, "+/-", u_tau)
print("T:", T, "+/-", u_T)
print("phi:", phi, "+/-", u_phi)
# prints the various values with uncertainties

plt.rcParams["figure.figsize"] = (10,3)
# Change the size of your plot - numbers are inches because USA

residual=ydata-fitfunction(xdata)
# find the residuals
zeroliney=[0,0]
zerolinex=[start,stop]
# create the line y=0

plt.errorbar(xdata,residual,yerr=yerror,xerr=xerror,fmt=".")
# plot the residuals with error bars
plt.plot(zerolinex,zeroliney)
# plotnthe y=0 line on top

plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (rad)")
plt.title("Residuals of Best Fit of Pendulum Amplitude over Time")
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph