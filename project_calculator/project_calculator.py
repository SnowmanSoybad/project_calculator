import tkinter as tk

class Application(tk.Tk):
    def __init__(self,root):
        self.root = root
        root.minsize(width=150, height=200)

        self.input_entry = tk.Entry(self.root)
        self.input_entry.pack(fill=tk.BOTH, expand=1)
        self.input_entry.bind("<Key>", lambda e: "break") 
        self.input_entry.pack(fill=tk.BOTH, expand=1)
        self.result = tk.Label(text = "result")
        self.result.pack()

        self.button_frame = tk.LabelFrame(self.root, text="Button")
        self.button_frame.pack(fill=tk.BOTH, expand=True)

        self.bt0 = tk.Button(self.button_frame, text="0",command= lambda :self.button_press("0"))
        self.bt0.grid(row=3, column=1, sticky="nesw")
        self.bt1 = tk.Button(self.button_frame, text="1",command= lambda :self.button_press("1"))
        self.bt1.grid(row=0, column=0, sticky="nesw")
        self.bt2 = tk.Button(self.button_frame, text="2",command= lambda :self.button_press("2"))
        self.bt2.grid(row=0, column=1, sticky="nesw")
        self.bt3 = tk.Button(self.button_frame, text="3",command= lambda :self.button_press("3"))
        self.bt3.grid(row=0, column=2, sticky="nesw")
        self.bt4 = tk.Button(self.button_frame, text="4",command= lambda :self.button_press("4"))
        self.bt4.grid(row=1, column=0, sticky="nesw")
        self.bt5 = tk.Button(self.button_frame, text="5",command= lambda :self.button_press("5"))
        self.bt5.grid(row=1, column=1, sticky="nesw")
        self.bt6 = tk.Button(self.button_frame, text="6",command= lambda :self.button_press("6"))
        self.bt6.grid(row=1, column=2, sticky="nesw")
        self.bt7 = tk.Button(self.button_frame, text="7",command= lambda :self.button_press("7"))
        self.bt7.grid(row=2, column=0, sticky="nesw")
        self.bt8 = tk.Button(self.button_frame, text="8",command= lambda :self.button_press("8"))
        self.bt8.grid(row=2, column=1, sticky="nesw")
        self.bt9 = tk.Button(self.button_frame, text="9",command= lambda :self.button_press("9"))
        self.bt9.grid(row=2, column=2, sticky="nesw")
        self.bt_plus = tk.Button(self.button_frame, text="+",command= lambda :self.button_press("+"))
        self.bt_plus.grid(row=0, column=3, sticky="nesw")
        self.bt_minus = tk.Button(self.button_frame, text="-",command= lambda :self.button_press("-"))
        self.bt_minus.grid(row=1, column=3, sticky="nesw")
        self.bt_mul = tk.Button(self.button_frame, text="*",command= lambda :self.button_press("*"))
        self.bt_mul.grid(row=3, column=0, sticky="nesw")
        self.bt_div = tk.Button(self.button_frame, text="/",command= lambda :self.button_press("/"))
        self.bt_div.grid(row=2, column=3, sticky="nesw")
        self.bt_ce = tk.Button(self.button_frame, text="CE", command=self.delete)
        self.bt_ce.grid(row=3, column=2, sticky="nesw")
        self.bt_cal = tk.Button(self.button_frame, text="=",command=self.calculate)
        self.bt_cal.grid(row=3, column=3, sticky="nesw")

        for x in range(4):
            tk.Grid.columnconfigure(self.button_frame, x, weight=1)
        for y in range(4):
            tk.Grid.rowconfigure(self.button_frame, y, weight=1)

    def button_press(self, text):
        self.input_entry.insert(tk.END, text)
    def delete(self):
        self.input_entry.delete(0, tk.END)
    def calculate(self):
        data = self.input_entry.get()
        result = eval(data)
        self.result["text"] = result


def mainapp():
    root = tk.Tk()
    app = Application(root)
    root.mainloop()

mainapp()