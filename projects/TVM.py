# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 13:35:24 2020

@author: Dan
"""
import numpy_financial as npf
import numpy as np
#TVM
class TVM(object):
    def __init__(self,n,iy,pv,pmt,fv):
        self.n=n
        self.iy=iy
        self.pv=pv
        self.pmt=pmt
        self.fv=fv
    def compound_int(pv,iy,n):
        comp_int=(pv*iy)*n
        print(comp_int, " in interest growth")
        
    def future_value(n,iy,pv):
        future_value=pv*(1+iy)**n
        print(future_value, " future value of inv")
    
    def discount_factor(iy,n):
        disc=1/(1+iy)**n
        print(str(round(disc,5)), ' discount factor')
        
TVM.compound_int(n=2,iy=.05,pv=100)
TVM.future_value(n=2,iy=.05,pv=100)
TVM.discount_factor(n=2,iy=.05)

inv=npf.pv(rate=.05, nper=10, pmt=0, fv=100000)
investment_2 = npf.fv(rate=.08, nper=10, pmt=0, pv=-100000)
print("Investment 2 will yield a total of $" + str(round(investment_2, 2)) + " in 10 years")
print(inv)
# Calculate investment_3
investment_3 = npf.fv(rate=.08, nper=10, pmt=0, pv=-100000)
print("Investment 3 will yield a total of $" + str(round(investment_3, 2)) + " in 10 years")

# Calculate investment_3 and adjsut for inflation of 3%
investment_3_discounted = npf.pv(rate=.03, nper=10, pmt=0, fv=investment_3)
print("After adjusting for inflation, investment 3 is worth $" + str(round(-investment_3_discounted, 2)) + " in today's dollars")

#Discounting cashflows with NPV
# NPV = sum of all discounted cashflows
cashflows = np.array([100,100,100,100,100])
npvinv1=npf.npv(rate=.03,values=cashflows)
print('NPV of INV1 is $',str(round(npvinv1,2))+" in today's dollars")

