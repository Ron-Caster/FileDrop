import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

def handle_drop(event):
    files = event.data
    for file in files:
        # Perform desired operations with the dropped file
        print("Dropped file:", file)

def create_gui():
    root = TkinterDnD.Tk()
    root.geometry("400x300")

    dropzone = tk.Label(root, text="Drop files here", width=30, height=10, relief=tk.RAISED)
    dropzone.pack(pady=50)

    dropzone.drop_target_register(DND_FILES)
    dropzone.dnd_bind('<<Drop>>', handle_drop)

    root.mainloop()

if __name__ == '__main__':
    create_gui()
