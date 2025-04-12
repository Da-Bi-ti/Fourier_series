import tkinter as tk
import Fourier_coefficient as FC
from sympy import sympify,pi,Function

an = Function("an")
bn = Function("bn")
# 創建 GUI
root = tk.Tk()
root.title('Fourier expand')
root.geometry('400x400')

#功能選擇
smooth_frame = tk.Frame(root)
piece_frame = tk.Frame(root)
def switch_input_mode():
    """ 根據選擇的模式顯示相應的輸入框 """
    if fn_type.get() == "Smooth function":

        smooth_frame.pack()
        piece_frame.pack_forget()
        
    else:

        smooth_frame.pack_forget()
        piece_frame.pack()
#函數類型
fn_type = tk.StringVar()
smooth_btn=tk.Radiobutton(root, text='Smooth function',variable=fn_type, value='Smooth function',command=switch_input_mode)
smooth_btn.pack()
smooth_btn.select()
piece_btn=tk.Radiobutton(root, text='Piecewise smooth function',variable=fn_type, value='Piecewise smooth function',command=switch_input_mode)
piece_btn.pack()
#展開類型
exp_type = tk.StringVar()
full_btn = tk.Radiobutton(root, text='fourier expandsion',variable=exp_type, value='fourier expandsion',command=switch_input_mode)
full_btn.pack()
full_btn.select()
half_btn=tk.Radiobutton(root, text='half_range expandsion',variable=exp_type, value='half_range expandsion',command=switch_input_mode)
half_btn.pack()
#########輸入標籤###########
#####smooth function######

tk.Label(smooth_frame, text="輸入函數:").pack()
f_in = tk.StringVar()
f_entry = tk.Entry(smooth_frame, textvariable=f_in, width=20)
f_entry.insert(0, "4-0.8*abs(t-5)")  # 預設函數
f_entry.pack()

tk.Label(smooth_frame, text="輸入週期:").pack()
Time = tk.StringVar()
T_entry = tk.Entry(smooth_frame, textvariable=Time, width=10)
T_entry.insert(0, "10")  # 預設週期
T_entry.pack()

# 顯示 Fourier 係數
result_label_a = tk.Label(root, text="an: ",font=20)
result_label_a.pack()

result_label_b = tk.Label(root, text="bn: ",font=20)
result_label_b.pack()

num_label = tk.Label(root, text="f= ",font=20)
num_label.pack()



# 顯示 Fourier 係數公式
def calculate_fourier():
    f = f_in.get()
    T = Time.get()
    tp = exp_type.get()
    try:
        global an
        global bn 
        if tp =="fourier expandsion":
            an, bn = FC.fourier_series(f, T)  # 取得回傳值
        elif tp =="half_range expandsion":
            an, bn = FC.half_range(f, T)
       
        result_label_a.config(text=f"an: {an}")  # 顯示 an
        result_label_b.config(text=f"bn: {bn}")  # 顯示 bn
        if tp == "fourier expandsion":
            num_label.config(text="f="+num_string()[0]+"\n"+num_string()[1]) # 顯示數值解 
        elif tp =="half_range expandsion":
            num_label.config(text="f_even="+num_string()[0]+"\nf_odd="+num_string()[1]) # 顯示數值解 
    except Exception as e:
        result_label_a.config(text="計算錯誤")
        result_label_b.config(text=str(e))  # 顯示錯誤訊息

######## 計算按鈕######
btn_calc = tk.Button(root, text="計算係數", command=calculate_fourier)
btn_calc.pack()

tk.Label(root, text="輸入項數:").pack()
Num = tk.StringVar()
N_entry = tk.Entry(root, textvariable=Num, width=10)
N_entry.insert(0, "4")  # 預設項數
N_entry.pack()
#########################
####係數數值#####

def num_string():
    N = int(Num.get())
    T = Time.get()
    T = sympify(T)
    omega=2*pi/T
    global an
    global bn

    (num_a,num_b)=FC.num_coefficient(an,bn,N)
    
    an_str=f"{num_a[0]}"
    bn_str=f"{num_b[0]}"
    #an
    for index,value in enumerate(num_a[1:-1],start=1):
        if value>=0 :
            an_str+=f"+{value}*cos({index}*{omega}t)"
        else:
            an_str+=f"{value}*cos({index}*{omega}t)"
    if num_a[N]>=0 :
        an_str+=f"+{num_a[N]}*cos({N}*{omega}t)+......"
    else:
        an_str+=f"{num_a[N]}*cos({N}*{omega}t)+......"
    #bn    
    for index,value in enumerate(num_b[1:-1],start=1):
        if value>=0 :
            bn_str+=f"+{value}*sin({index}*{omega}t)"
        else:
            bn_str+=f"{value}*sin({index}*{omega}t)"
    if num_a[N]>=0 :
        bn_str+=f"+{num_a[N]}*sin({N}*{omega}t)+......"
    else:
        bn_str+=f"{num_a[N]}*sin({N}*{omega}t)+......"
    return (an_str,bn_str)


#######piecewise########

text = tk.Text(piece_frame, height=5, width=50)  # 放入多行輸入框
text.pack()
tk.Label(piece_frame, text="輸入週期:").pack()
Time = tk.StringVar()
T_entry = tk.Entry(piece_frame, textvariable=Time, width=10)
T_entry.insert(0, "10")  # 預設週期
T_entry.pack()




# 預設顯示一般函數輸入框
smooth_frame.pack()
piece_frame.pack_forget()
# 啟動 GUI
root.mainloop()