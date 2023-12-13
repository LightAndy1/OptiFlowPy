import os
import tkinter as tk
from tkinter import filedialog


def process_files(input_folder, file_size_limit_mb):
    # Your file processing logic here
    # This is just a placeholder function

    print(f"Processing files in folder: {input_folder}")
    print(f"File size limit: {file_size_limit_mb} MB")


def select_folder():
    folder_path = filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(0, folder_path)


def start_processing():
    input_folder = entry_folder.get()
    file_size_limit_mb = int(slider_file_size.get())

    process_files(input_folder, file_size_limit_mb)


# Create the main window
root = tk.Tk()
root.title("File Manager")

# Input Folder
label_folder = tk.Label(root, text="Select Input Folder:")
label_folder.pack()

entry_folder = tk.Entry(root, width=50)
entry_folder.pack()

btn_browse = tk.Button(root, text="Browse", command=select_folder)
btn_browse.pack()

# File Size Limit Slider
label_file_size = tk.Label(root, text="Set File Size Limit (MB):")
label_file_size.pack()

slider_file_size = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL)
slider_file_size.pack()

# Buttons
btn_enter = tk.Button(root, text="Enter", command=start_processing)
btn_enter.pack()

btn_go_to_folder = tk.Button(
    root, text="Go to Folder", command=lambda: os.startfile(entry_folder.get())
)
btn_go_to_folder.pack()

# Start the GUI event loop
root.mainloop()
