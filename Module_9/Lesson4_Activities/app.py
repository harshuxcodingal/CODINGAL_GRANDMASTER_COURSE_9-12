import tkinter as tk

# Create window
root = tk.Tk()
root.title("Tkinter - 2")
root.geometry("350x250")

# Label
label = tk.Label(root, text="Enter Your Name:", font=("Arial", 12))
label.pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Function
def show_name():
    name = entry.get()
    result_label.config(text="Hello " + name)

# Button
btn = tk.Button(root, text="Submit", command=show_name)
btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run window
root.mainloop()