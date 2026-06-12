import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Tkinter Combined Program")
root.geometry("500x500")

# ---------------- IMAGE SECTION ----------------
label_title = tk.Label(root, text="Image Makes It Better", font=("Arial", 14))
label_title.pack(pady=10)

try:
    img = Image.open("image.jpg")   # put your image file here
    img = img.resize((200, 200))
    photo = ImageTk.PhotoImage(img)

    img_label = tk.Label(root, image=photo)
    img_label.pack(pady=10)

except:
    img_label = tk.Label(root, text="Image not found!", fg="red")
    img_label.pack(pady=10)

# ---------------- VIRUS ALERT ----------------
def virus_alert():
    messagebox.showwarning("Alert!", "Virus Detected!")

btn_alert = tk.Button(root, text="Scan System (Virus Alert)", command=virus_alert)
btn_alert.pack(pady=10)

# ---------------- TOP LEVEL WINDOW ----------------
def open_window():
    top = tk.Toplevel()
    top.title("Top Level Window")
    top.geometry("300x200")

    tk.Label(top, text="This is a new window!", font=("Arial", 12)).pack(pady=40)

    tk.Button(top, text="Close", command=top.destroy).pack()

btn_window = tk.Button(root, text="Open New Window", command=open_window)
btn_window.pack(pady=10)

# ---------------- EXIT BUTTON ----------------
exit_btn = tk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(pady=20)

# ---------------- RUN APP ----------------
root.mainloop()