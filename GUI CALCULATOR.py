import tkinter as tk

def subtract():
    a = int(x.get())
    b = int(y.get())
    answer.config(text=a - b)

root = tk.Tk()
root.title("Calculator")

x = tk.Entry(root)
x.pack()

y = tk.Entry(root)
y.pack()

tk.Button(root, text="Subtract", command=subtract).pack()

answer = tk.Label(root, text="")
answer.pack()

root.mainloop()
