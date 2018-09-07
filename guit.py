try:                        # In order to be able to import tkinter for
    import tkinter as tk    # either in python 2 or in python 3
except ImportError:
    import Tkinter as tk


def add_four_entries():
    global root, my_list_of_entries
    for _ in range(4):
        my_list_of_entries.append(tk.Entry(root))
        my_list_of_entries[-1].pack()


if __name__ == '__main__':
    root = tk.Tk()
    my_list_of_entries = list()
    tk.Button(root, text="Add 4 more", command=add_four_entries).pack()
    tk.mainloop()