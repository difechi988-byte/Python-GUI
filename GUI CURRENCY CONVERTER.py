import tkinter as tk

def change():
    n = float(naira.get())
    result.config(text="Euro: " + str(n / 1600))

app = tk.Tk()
app.title("Currency App")

tk.Label(app, text="Naira").pack()
naira = tk.Entry(app)
naira.pack()

tk.Button(app, text="Convert to Euro", command=change).pack()

result = tk.Label(app, text="")
result.pack()

app.mainloop()
