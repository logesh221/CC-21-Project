import tkinter as tk
from Automated_screen_shots_functions import screen_shot, time__table


def show(frame):
    frame.tkraise()


x = 600
y = 400
root = tk.Tk()
root.geometry("{}x{}".format(x, y))
root.title('Automated_screen_shots')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame1 = tk.Frame(root, bg="light blue")
frame2 = tk.Frame(root, bg="light blue")
frame3 = tk.Frame(root, bg="light blue")
frame4 = tk.Frame(root, bg="light blue")

for i in (frame1, frame2, frame3, frame4):
    i.grid(row=0, column=0, sticky="nsew")

# ========================frame1===========================

tk.Label(frame1, text='Screen shots saver', font=' Fixedsys 20 bold', fg="black",
         background="light blue").grid(row=0, column=0, ipadx=20, ipady=10)

tk.Label(frame1, text='The League', font='arial 15 bold', fg="white",
         background="light blue").grid(row=2, column=0, ipadx=(x // 2) - 60, ipady=10)

tk.Button(frame1, text="Take screen shots", font='Fixedsys 5 bold', fg='white', bg='blue', width=30,
          command=lambda: show(frame2)).grid(row=1, column=0, ipadx=10, ipady=10)
show(frame1)

# =======================frame2==============================

tk.Label(frame2, background="light blue").grid(row=0, column=0)

tk.Button(frame2, background="blue", command=lambda: show(frame3), text='Just save to a dir',
          font='Fixedsys 5 ', fg='white').grid(row=1, column=0, ipadx=10, ipady=10)

tk.Label(frame2, text='or', background="light blue").grid(row=2, column=0)

tk.Button(frame2, background='blue', fg='white', text='Save with reference to a time table',
          command=lambda: show(frame4),
          font='Fixedsys 5 ').grid(row=3, column=0, ipadx=10, ipady=10)
tk.Label(frame2, fg="light blue",
         background="light blue").grid(row=4, column=0)

tk.Button(frame2, background="red", text='Back', fg="white",
          font='Fixedsys 5 ', command=lambda: show(frame1), width=10).grid(row=5, column=0, ipadx=10, ipady=10)

tk.Label(frame2, text='The League', font='arial 15 bold', fg="white",
         background="light blue").grid(row=6, column=0, ipadx=(x // 2) - 50, ipady=10)

# =======================frame3==============================


time_limit = tk.IntVar()
path_0 = tk.StringVar()

tk.Label(frame3, text='Enter the full path', font='Fixedsys 5',
         background="light blue").grid(row=0, column=0, ipadx=(x // 2) - 70, ipady=10)

tk.Entry(frame3, textvariable=path_0, bg='linen', width=33).grid(row=1, column=0, ipadx=10, ipady=10)

tk.Label(frame3, text='Enter the Time limit', font='Fixedsys 5',
         background="light blue").grid(row=2, column=0, ipadx=(x // 2) - 70, ipady=10)
tk.Entry(frame3, textvariable=time_limit, bg='linen', width=33).grid(row=3, column=0, ipadx=10, ipady=10)

tk.Label(frame3, fg="light blue",  # blank space
         background="light blue").grid(row=4, column=0)

tk.Button(frame3, background="blue", text='Start', fg="white",
          font='Fixedsys 5 ', command=lambda: screen_shot(path_0.get(), time_limit.get()),
          width=10).grid(row=5, column=0, ipadx=10, ipady=10)

tk.Label(frame3, fg="light blue",  # blank space
         background="light blue").grid(row=6, column=0)

tk.Button(frame3, background="red", text='Back', fg="white",
          font='Fixedsys 5 ', command=lambda: show(frame2), width=10).grid(row=7, column=0, ipadx=10, ipady=10)

tk.Label(frame3, text='The League', font='arial 15 bold', fg="white",
         background="light blue").grid(row=8, column=0, ipadx=(x // 2) - 50, ipady=10)

# =======================frame4==============================
time_table = tk.StringVar()
path_1 = tk.StringVar()

tk.Label(frame4, text='Enter the Time Table\n eg:sub_name1:duration sub_name2:d....', font='Fixedsys 5',
         background="light blue").grid(row=0, column=0, ipadx=(x // 2) - 150, ipady=10)

tk.Entry(frame4, textvariable=time_table, bg='linen', width=33).grid(row=1, column=0, ipadx=10, ipady=10)

tk.Label(frame4, text='Enter the full Path', font='Fixedsys 5',
         background="light blue").grid(row=2, column=0, ipadx=(x // 2) - 100, ipady=10)
tk.Entry(frame4, textvariable=path_1, bg='linen', width=33).grid(row=3, column=0, ipadx=10, ipady=10)

tk.Label(frame4, fg="light blue",
         background="light blue").grid(row=4, column=0)

tk.Button(frame4, background="blue", text='Start', fg="white",
          command=lambda: time__table(time_table.get(), path_1.get()),
          font='Fixedsys 5 ', width=10).grid(row=5, column=0, ipadx=10, ipady=10)

tk.Label(frame4, fg="light blue",
         background="light blue").grid(row=6, column=0)

tk.Button(frame4, background="red", text='Back', fg="white",
          font='Fixedsys 5 ', command=lambda: show(frame2), width=10).grid(row=7, column=0, ipadx=10, ipady=10)

tk.Label(frame4, text='The League', font='arial 15 bold', fg="white",
         background="light blue").grid(row=8, column=0, ipadx=(x // 2) - 50, ipady=10)

root.mainloop()