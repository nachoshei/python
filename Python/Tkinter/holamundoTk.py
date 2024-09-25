import tkinter as tk

root = tk.Tk()

root.title("Hola Mundo con Tkinter")

root.geometry("300x200")

label = tk.Label(root, text= "¡Hola Mundo!", font=("Arial", 10))
#label.pack(pady=50)

label.pack(expand=True)
#label.pack(padx=75)
#label.pack(anchor="center")

root.mainloop()