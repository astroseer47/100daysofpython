import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=400)


# Label
new_label = tkinter.Label(text="This is new text", font=("Arial", 25))
new_label.pack()
# new_label.place(x=0, y=0)
# new_label.grid(column=0, row=0)

# Entry - Inputs
input1 = tkinter.Entry(width=20)
input1.pack()
print(input1.get())

# Buttons
def handle_click():
    global input1
    print("Clicked")
    new_label["text"] = "Clicked!"
    new_label["text"] = input1.get()
button = tkinter.Button(text="Click me", command=handle_click)
button.pack()








window.mainloop()