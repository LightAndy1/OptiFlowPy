import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from src.compressor import compress_image


class OptiFlowPyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OptiFlowPy")
        self.root.geometry("420x150")
        icon_path = os.path.join("assets", "icon.png")
        if os.path.exists(icon_path):
            root.iconphoto(True, tk.PhotoImage(file=icon_path))

        self.input_folder_path = tk.StringVar()
        self.output_folder_path = tk.StringVar()
        self.compression_percentage = tk.DoubleVar(value=75)

        self.create_widgets()

    def create_widgets(self):
        # ^ Labels
        tk.Label(self.root, text="Input Folder:").grid(row=0, column=0, sticky="e")
        tk.Label(self.root, text="Output Folder:").grid(row=1, column=0, sticky="e")
        tk.Label(self.root, text="Compression Percentage:").grid(
            row=2, column=0, sticky="e"
        )

        # ^ Entry Widgets
        ttk.Entry(
            self.root, textvariable=self.input_folder_path, state="readonly"
        ).grid(row=0, column=1, sticky="ew")
        ttk.Entry(
            self.root, textvariable=self.output_folder_path, state="readonly"
        ).grid(row=1, column=1, sticky="ew")

        # ^ Buttons
        ttk.Button(self.root, text="Browse", command=self.browse_input_folder).grid(
            row=0, column=2
        )
        ttk.Button(self.root, text="Browse", command=self.browse_output_folder).grid(
            row=1, column=2
        )
        ttk.Button(
            self.root, text="Compress Images", command=self.compress_images
        ).grid(row=3, column=1, pady=10)

        # ^ Slider
        ttk.Scale(
            self.root,
            from_=1,
            to=100,
            variable=self.compression_percentage,
            orient="horizontal",
            length=200,
        ).grid(row=2, column=1, pady=10)

    def browse_input_folder(self):
        folder_selected = filedialog.askdirectory()
        self.input_folder_path.set(folder_selected)

    def browse_output_folder(self):
        folder_selected = filedialog.askdirectory()
        self.output_folder_path.set(folder_selected)

    def compress_images(self):
        input_folder = self.input_folder_path.get()
        output_folder = self.output_folder_path.get()
        compression_percentage = int(self.compression_percentage.get())

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        try:
            for file_name in os.listdir(input_folder):
                if file_name.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                    input_path = os.path.join(input_folder, file_name)
                    output_path = os.path.join(output_folder, file_name)
                    compress_image(input_path, output_path, compression_percentage)

            messagebox.showinfo("Success", "Image compression completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = OptiFlowPyApp(root)
    root.mainloop()
