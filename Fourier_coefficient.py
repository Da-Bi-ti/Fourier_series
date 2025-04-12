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
        # 取出每个分段
        pw = an.args[1] if isinstance(an.args[1], Piecewise) else None
        # 檢查
        if pw:
            pieces = list(pw.args)
            # 例如：修改第二段的值
            pieces[1] = (pieces[1][0]/2, pieces[1][1])  #更正首項為二分之一
            pw_new = Piecewise(*pieces)
            an = an.args[0] * pw_new
        bn = (2/T) * integrate(f * sin(n*(2*pi/T)*t), (t, 0, T))
        simplified_an= simplify_logic(an)
        simplified_bn= simplify_logic(bn)
        return simplified_an,simplified_bn
        
    except Exception as e:
        print(e)
        

###以奇偶函數展開###

def half_range(f,T):
    f=sympify(f)
    T=sympify(T)
    print("f=",f,"  T=",T)
    w = symbols("w",commutative=True)
    w = 2*pi/T

    try:
        #公式
        an = 2*(2/T) * integrate(f * cos(n*w*t), (t, 0, T/2))
        pw = an.args[1] if isinstance(an.args[1], Piecewise) else None #剔除公式係數(如果有)
        # 檢查
        if pw:
            pieces = list(pw.args) #pw.args回傳tuple:((函數1，區間1),(函數2，區間2)...)
            pieces[1] = (pieces[1][0]/2, pieces[1][1])  #更正首項為二分之一
            pw_new = Piecewise(*pieces)
            an = an.args[0] * pw_new
        
        bn = 2*(2/T) * integrate(f * sin(n*w*t), (t, 0, T/2))
        simplified_an= simplify_logic(an)
        simplified_bn= simplify_logic(bn)
        return(simplified_an,simplified_bn) 
    except Exception as e:
        print(e)
    
"""
    if _name_==_main_:
        print("if you want to extended as \"even function(cos)\": look an\n"
              "if you want to extended as \"odd function(sine)\": look bn\n")
        print("formula:\n"
              "an=",an,"\n\n"
              "bn=",bn)
"""

    

#####計算前k項數值#######
def num_coefficient(an,bn,k):

    an_list=[]
    bn_list=[]
    try:
        for i in range(k+1):
            an_list.append(round(an.subs(n,i).evalf(),precise))
            bn_list.append(round(bn.subs(n,i).evalf(),precise))
        
        return(an_list,bn_list)
    
    except TypeError :
        for i in range(k+1):
            an_list.append(an.subs(n,i))
            bn_list.append(bn.subs(n,i))
        return(an_list,bn_list)
    except Exception as e:
        print(e)

    
    
if __name__ == '__main__':

    print(fourier_series())
    print(num_coefficient(3))  
    
    
    
    
    
    