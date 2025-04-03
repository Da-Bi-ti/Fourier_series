import tkinter as tk
import Fourier_coefficient as FC

# 創建 GUI
root = tk.Tk()
root.title('Fourier expand')
root.geometry('400x400')

# 輸入標籤
tk.Label(root, text="輸入函數:").pack()
function = tk.StringVar()
f_entry = tk.Entry(root, textvariable=function, width=20)
f_entry.insert(0, "4-0.8*abs(t-5)")  # 預設函數
f_entry.pack()

tk.Label(root, text="輸入週期:").pack()
Time = tk.StringVar()
T_entry = tk.Entry(root, textvariable=Time, width=10)
T_entry.insert(0, "10")  # 預設週期
T_entry.pack()

# 顯示 Fourier 係數
result_label_a = tk.Label(root, text="an: ")
result_label_a.pack()

result_label_b = tk.Label(root, text="bn: ")
result_label_b.pack()

# 計算 Fourier 係數
def calculate_fourier():
    f = function.get()
    T = Time.get()

    try:
        an, bn = FC.fourier_series(f, T)  # 取得回傳值
        result_label_a.config(text=f"an: {an}")  # 顯示 an
        result_label_b.config(text=f"bn: {bn}")  # 顯示 bn
    except Exception as e:
        result_label_a.config(text="計算錯誤")
        result_label_b.config(text=str(e))  # 顯示錯誤訊息

# 計算按鈕
btn_calc = tk.Button(root, text="計算係數", command=calculate_fourier)
btn_calc.pack()

# 啟動 GUI
root.mainloop()
