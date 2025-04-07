from __future__ import division
from sympy import *
import tkinter as tk


t = symbols('t',commutative=True)
n = symbols("n",commutative=True)
precise = 3 #係數保留至小數點下n位
    
#####一般週期函數#####   
def fourier_series(f=4-0.8*abs(t-5),T=10):
    try:
        #讀取週期、函數
        f=sympify(f)
        T=sympify(T)
        print("f=",f,"  T=",T)
        ######

        an = (2/T) * integrate(f * cos(n*(2*pi/T)*t), (t, 0, T))
        bn = (2/T) * integrate(f * sin(n*(2*pi/T)*t), (t, 0, T))
        global simplified_an 
        global simplified_bn
        simplified_an= simplify_logic(an)
        simplified_bn= simplify_logic(bn)
        return(simplified_an,simplified_bn)
        
    except Exception as e:
        print(e)
        

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
#####計算前k項數值#######
def num_coefficient(k):
    an_list=[]
    bn_list=[]
    for i in range(k+1):
        an_list.append(round(simplified_an.subs(n,i).evalf(),precise))
        bn_list.append(round(simplified_bn.subs(n,i).evalf(),precise))
    
    return(an_list,bn_list)
    
    
    
if __name__ == '__main__':

    print(fourier_series())
    print(num_coefficient(3))  
    
    
    
    
    
    