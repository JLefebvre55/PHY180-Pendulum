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
MICHAL'S MODIFICATION
The function to be fitted is now k * (L_naught +L)**n
The plots all have bigger labels (I kept losing marks for them)
Labels are global so you only need to enter them once
If you want to learn some formatting yourself, check out this documentation:
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot and scroll to the bottom
or https://matplotlib.org/3.1.1/api/text_api.html#matplotlib.text.Text for labels and other texty things

Line 42: replace with your filename
Lines 44-47: replace with axis labels (these will be the same on both normal and loglog plot. you can change that by replacing the variable name in the label)
Line 108: Replace with title for normal plot
Line 136: Replace with title for residual plot
Line 156: Replace with title for residual, loglog plot
Line 184: Replace with title for normal, loglog plot
"""
filename="../data/q4a_data.txt"

xlabel = "Length (m)"
ylabel = "Period (sec)"
xlabel_residuals = "Length (m)"
ylabel_residuals = "Period (sec)"

# change this if your filename is different


import scipy.optimize as optimize
import numpy as np
import matplotlib.pyplot as plt
from pylab import loadtxt
import math

data=loadtxt(filename, usecols=(0,1,2,3), skiprows=1, unpack=True)
# load filename, take columns 0 & 1 & 2 & 3, skip 1 row, unpack=transpose x&y

xdata=data[0]
ydata=data[1]
xerror=data[2]
yerror=data[3]
# finished importing data, naming it sensibly


def my_func(L, k, L_naught, n):
    return k*(L_naught +L)**n
# this is the function we want to fit. the first variable must be the
# x-data (length), the rest are the unknown constants we want to determine

popt, pcov = optimize.curve_fit(my_func, xdata, ydata)
# we have the best fit values in popt[], while pcov[] tells us the uncertainties

k=popt[0]
L_naught=popt[1]
n=popt[2]
# best fit values are named nicely

u_k=pcov[0,0]**(0.5)
u_L_naught=pcov[1,1]**(0.5)
u_n=pcov[2,2]**(0.5)
# uncertainties of fit are named nicely

def fitfunction(L):
    return k * (L_naught +L)**n
#fitfunction(t) gives you your ideal fitted function, i.e. the line of best fit

start=min(xdata)
stop=max(xdata)
xs=np.arange(start,stop,(stop-start)/1000) # fit line has 1000 points
curve=fitfunction(xs)
# (xs,curve) is the line of best fit for the data in (xdata,ydata)

plt.rcParams["figure.figsize"] = (10,6)
# Change the size of your plot - numbers are inches because USA

# add triple quotes here to generate loglog plot
'''
plt.errorbar(xdata,ydata,yerr=yerror,xerr=xerror,fmt=".")
# plot the data, fmt makes it data points not a line
plt.plot(xs,curve)
# plot the best fit curve on top of the data points as a line

plt.xlabel(xlabel, fontsize=14)
plt.ylabel(ylabel, fontsize=14)
plt.title("Fit of Power Law Function on Period vs Length", fontsize = 14)
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph


print("k:", k, "+/-", u_k)
print("L_naught:", L_naught, "+/-", u_L_naught)
print("n:", n, "+/-", u_n)
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

plt.xlabel(xlabel_residuals, fontsize=14)
plt.ylabel(ylabel_residuals, fontsize=14)
plt.title("Residual of Fit of Power Law Function on Period vs Length", fontsize = 14)
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph

'''
# The loglog plot
# (same as above, with all the plot commands changed to log)
# Remove ending triple quotes to use
# For some reason I can only plot one thing at a time so I comment out the plots I don't currently need


plt.errorbar(xdata,ydata,yerr=yerror,xerr=xerror,fmt=".")
# plot the data, fmt makes it data points not a line
plt.loglog(xs,curve)
# plot the best fit curve on top of the data points as a line

plt.xlabel(xlabel, fontsize=14)
plt.ylabel(ylabel, fontsize=14)
plt.title("Fit of Power Law Function on Period vs Length (LOG)", fontsize = 14)
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph


print("k:", k, "+/-", u_k)
print("L_naught:", L_naught, "+/-", u_L_naught)
print("n:", n, "+/-", u_n)
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
plt.loglog(zerolinex,zeroliney)
# plotnthe y=0 line on top

plt.xlabel(xlabel_residuals, fontsize=14)
plt.ylabel(ylabel_residuals, fontsize=14)
plt.title("Residual of Fit of Power Law Function on Period vs Length (LOG)", fontsize = 14)
# HERE is where you change how your graph is labelled!

plt.show()
# show the graph