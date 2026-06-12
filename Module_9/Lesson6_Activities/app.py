import tkinter as tk

# Function to calculate denominations
def calculate():
    amount = int(entry.get())

    notes_2000 = amount // 2000
    amount %= 2000

    notes_500 = amount // 500
    amount %= 500

    notes_200 = amount // 200
    amount %= 200

    notes_100 = amount // 100
    amount %= 100

    notes_50 = amount // 50
    amount %= 50

    result_label.config(
        text=f"2000 x {notes_2000}\n"
             f"500 x {notes_500}\n"
             f"200 x {notes_200}\n"
             f"100 x {notes_100}\n"
             f"50 x {notes_50}\n"
             f"Remaining: {amount}"
    )

# Main window
root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("350x400")

# Input label
tk.Label(root, text="Enter Amount:", font=("Arial", 12)).pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)

# Button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Run app
root.mainloop()