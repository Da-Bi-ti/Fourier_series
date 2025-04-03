from __future__ import division
from sympy import *
import tkinter as tk

#####一般週期函數#####
t = symbols('t',commutative=True)
n = symbols("n",commutative=True)
def fourier_series(f=4-0.8*abs(t-5),T=10):
    try:
        #讀取週期、函數
        f=sympify(f)
        T=sympify(T)
        print("f=",f,"  T=",T)
        ######

        an = (2/T) * integrate(f * cos(n*t), (t, 0, T))
        bn = (2/T) * integrate(f * sin(n*t), (t, 0, T))
        an=simplify(an)
        bn=simplify(bn)
        return (an,bn)
        
    except Exception as e:
        print(e)
        
       
if __name__ == '__main__':
    fourier_series()



###以奇偶函數展開###
"""
def half_range(f,T):
    t = symbols('t',commutative=True)
    T = 20
    w = symbols("w",commutative=True)
    w = 2*pi/T
    f = 4-0.8*abs(t-5)  # Define your function
    n = symbols("n",commutative=True)


    #公式
    an = 2*(2/T) * integrate(f * cos(n*w*t), (t, 0, T/2))
    bn = 2*(2/T) * integrate(f * sin(n*w*t), (t, 0, T/2))
    if _name_==_main_:
        print("if you want to extended as \"even function(cos)\": look an\n"
              "if you want to extended as \"odd function(sine)\": look bn\n")
        print("formula:\n"
              "an=",an,"\n\n"
              "bn=",bn)
    
#計算並回傳
for n in range(0,4):
    a0 = 2*(2/T) * integrate(f, (t, 0, T/2))
    an = 2*(2/T) * integrate(f * cos(n*w*t), (t, 0, T/2))
    bn = 2*(2/T) * integrate(f * sin(n*w*t), (t, 0, T/2))
    print(f"n={n}:\n")
    print("an=",an.evalf())
    print("bn=",bn.simplify(),"\n")
"""

