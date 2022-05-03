from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    root = Tk()
    root.title('Resize Sizegrip')
    root.minsize(300, 200)
    root.columnconfigure(0, weight=1);
    root.rowconfigure(0, weight=1);

    # サイズグリップ
    sizegrip = ttk.Sizegrip(root)
    sizegrip.grid(row=1, column=0, sticky=(S, E))

    # フレーム
    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0, sticky=(N, W, S, E))
    frame.columnconfigure(0, weight=1);
    frame.rowconfigure(0, weight=1);

    # ボタン
    button1 = ttk.Button(
        frame, width=5,
        text='OK', command=quit)
    button1.grid(row=0, column=0, sticky=(S, E))

    root.mainloop()