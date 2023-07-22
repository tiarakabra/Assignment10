import tkinter as tk
import webbrowser

def open_website():
    url = entry.get()
    webbrowser.open(url)


root = tk.Tk()
root.title("Web Browser")


window_width = 400
window_height = 150


label = tk.Label(root, text="Enter the URL:")
label.pack(pady=10)


entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Ok", command=open_website)
button.pack(pady=10)

def on_closing():
    print("Exiting the application...")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
