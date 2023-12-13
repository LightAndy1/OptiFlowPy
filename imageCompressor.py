import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image


def compress_images(input_folder, output_folder, file_size_limit_kb):
    # Check if the output folder exists, create if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(input_path) as img:
                img.save(output_path, quality=file_size_limit_kb)

    print(f"Image compression completed. Output folder: {output_folder}")


def select_folder():
    folder_path = filedialog.askdirectory()
    entry_folder.delete(0, tk.END)
    entry_folder.insert(0, folder_path)

    default_output_folder = os.path.join(folder_path, "OptiFlowPy - Output")
    entry_output_folder.delete(0, tk.END)
    entry_output_folder.insert(0, default_output_folder)


def start_processing():
    input_folder = entry_folder.get()
    output_folder = entry_output_folder.get()
    file_size_limit_kb = int(slider_file_size.get())

    compress_images(input_folder, output_folder, file_size_limit_kb)


# Create the main window
root = tk.Tk()
root.title("Image Compressor")

# Input Folder
label_folder = tk.Label(root, text="Select Input Folder:")
label_folder.pack()

entry_folder = tk.Entry(root, width=50)
entry_folder.pack()

btn_browse = tk.Button(root, text="Browse", command=select_folder)
btn_browse.pack()

# Output Folder
label_output_folder = tk.Label(root, text="Select Output Folder:")
label_output_folder.pack()

entry_output_folder = tk.Entry(root, width=50)
entry_output_folder.pack()

# File Size Limit Slider
label_file_size = tk.Label(root, text="Set File Size Limit (KB):")
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
