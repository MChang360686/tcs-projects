import tkinter as tk

window = tk.Tk()

def buttonClicked():
    label2["text"] = "Button was clicked"       

label = tk.Label(text="Click on the button")
label2 = tk.Label(text="")
button = tk.Button(text = "I like spaghetti", command=buttonClicked)

label.pack()
label2.pack()
button.pack()

window.mainloop()