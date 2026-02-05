from tkinter import *

window = Tk()
window.minsize(width=500, height=400)
window.title("Mile to KM Converter")

miles_input = Entry()
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

km_result = Label(text="0")
km_result.grid(row=1, column=1)

km_label = Label(text="KM")
km_label.grid(row=1, column=2)

def handle_calculate():
    miles = int(miles_input.get())
    km = round(miles * 1.6, 2)
    km_result.config(text=str(km))


button = Button(text="Calculate", command=handle_calculate)
button.grid(row=2, column=1)












window.mainloop()