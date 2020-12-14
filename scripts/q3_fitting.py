# -*- coding: utf-8 -*-
"""
README
This program imports data from the file specified by the string filename
The first line of the file is ignored (assuming it's the name of the variables)
After that the data file needs to be formatted: 
number space number space number space number newline
Do NOT put commas in your data file!!
The data file should be in the same directory as this python file
The data should be in the order:
x_data y_data x_uncertainty y_uncertainty
Then this program tries to fit a function to the data points
It plots the data as dots with errorbars and the best fit line
It then prints the best fit information
After that, it plots the "residuals": ydata - fittedfunction(xdata)
That is it subtracts your fitted ideal values from your actual data to see 
what is "left over" from the fit
Ideally your residuals graph should look like noise, otherwise there is more
information you could extract from your data (or you used the wrong fitting
function)
If you want to change the graph labels, look for the plt.xlabel() commands
If you want to change the file name, that's the next line below this comment

RYAN'S MODIFICATION
the function to be fitted is now A + Btheta0 + Ctheta0^2
if you scroll down, you will see on the right side lines suggesting you modify parts of the program, the line numbers are listed here

Line 51: replace with your filename
Line 110-112: Replace with Axis Names and title
Line 138-140: Replace with Axis Names and title for residual plot

you can use this sample data to test it work on your machine

theta0 period dtheta0 dperiod
-3 2.5 0 0
-2 1.6 0 0
-1 0.9 0 0
0 0.4 0 0
1 0.1 0 0
2 0.0 0 0
3 0.1 0 0
4 0.4 0 0
5 0.9 0 0
6 1.6 0 0
7 2.5 0 0
Should be around (note that the uncertainties might look like 1.1678697877033738e-17, which means 0)
A: 0.4 +/- 0
B: -0.4 +/- 0
C: 0.1 +/- 0
"""
filename="../data/q4b_summary.txt"
# change this if your filename is different

import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt
import math

data=loadtxt(filename, usecols=(0,1,2,3), skiprows=1, unpack=True)
# load filename, take columns 0 & 1 & 2 & 3, skip 1 row, unpack=transpose x&y
# b = 100
# a = 0
# xdata=np.array(data[0][a:b])
# ydata=np.array(data[1][a:b])
# xerror=np.array(data[2][a:b])
# yerror=np.array(data[3][a:b])
xdata = data[0]
ydata = data[1]
xerror = data[2]
yerror = data[3]
# finished importing data, naming it sensibly

# This is just for me because my ydata needs to be scaled based on how I collected it
# ydata *= math.pi / 30
# scaling ydata

def my_func(theta0, A, B, C):
    return A + B*theta0 + C*theta0**2
# this is the function we want to fit. the first variable must be the
# x-data (time), the rest are the unknown constants we want to determine

popt, pcov = optimize.curve_fit(my_func, xdata, ydata)
# we have the best fit values in popt[], while pcov[] tells us the uncertainties

A=popt[0]
B=popt[1]
C=popt[2]
# best fit values are named nicely

u_A=pcov[0,0]**(0.5)
u_B=pcov[1,1]**(0.5)
u_C=pcov[2,2]**(0.5)
# uncertainties of fit are named nicely

def fitfunction(t):  
    return A + B*t + C*t**2
#fitfunction(t) gives you your ideal fitted function, i.e. the line of best fit

start=min(xdata)
stop=max(xdata)    
xs=np.arange(start,stop,(stop-start)/1000) # fit line has 1000 points
curve=fitfunction(xs)
# (xs,curve) is the line of best fit for the data in (xdata,ydata) 

plt.rcParams["figure.figsize"] = (10,6)
# Change the size of your plot - numbers are inches because USA

plt.errorbar(xdata,ydata,yerr=yerror,xerr=xerror,fmt=".")
# plot the data, fmt makes it data points not a line
plt.plot(xs,curve)
# plot the best fit curve on top of the data points as a line

plt.xlabel("Starting Amplitude (rad)")
plt.ylabel("Period (sec)")
plt.title("Power Series Fit of Pendulum Period vs Amplitude")
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph


print("A:", A, "+/-", u_A)
print("B:", B, "+/-", u_B)
print("C:", C, "+/-", u_C)
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

plt.xlabel("Amplitude Error (rad)")
plt.ylabel("Period Error (sec)")
plt.title("Residuals of Power Series Fit of Period vs Amplitude")
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph