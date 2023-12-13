import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageSequence
import imageio
import shutil


def compress_images(input_folder, output_folder, target_size_mb):
    # Check if the output folder exists, create if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            input_path = os.path.join(root, filename)
            relative_path = os.path.relpath(input_path, input_folder)
            output_path = os.path.join(output_folder, relative_path)

            if not os.path.exists(os.path.dirname(output_path)):
                os.makedirs(os.path.dirname(output_path))

            compress_single_image(input_path, output_path, target_size_mb)

    print(f"Image compression completed. Output folder: {output_folder}")


def compress_single_image(input_path, output_path, target_size_mb):
    try:
        with Image.open(input_path) as img:
            # Calculate the compression ratio based on the desired output file size
            compression_ratio = target_size_mb / (
                os.path.getsize(input_path) / (1024 * 1024)
            )

            # Save as a temporary file with reduced quality and adjusted compression ratio
            temp_path, temp_extension = os.path.splitext(output_path)
            temp_path += "_temp" + temp_extension
            img.save(temp_path, quality=int(85 * compression_ratio))

            # Move the temporary file to the final output path
            shutil.move(temp_path, output_path)

    except Exception as e:
        print(f"Error compressing {input_path}: {e}")


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
    target_size_mb = float(entry_target_size.get())

    compress_images(input_folder, output_folder, target_size_mb)


# Create the main window
root = tk.Tk()
root.title("Advanced Image Compressor")

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

# Target Size Entry
label_target_size = tk.Label(root, text="Enter Target Output Size (MB):")
label_target_size.pack()

entry_target_size = tk.Entry(root)
entry_target_size.pack()

# Buttons
btn_enter = tk.Button(root, text="Enter", command=start_processing)
btn_enter.pack()

btn_go_to_folder = tk.Button(
    root, text="Go to Folder", command=lambda: os.startfile(entry_folder.get())
)
btn_go_to_folder.pack()

# Start the GUI event loop
root.mainloop()
