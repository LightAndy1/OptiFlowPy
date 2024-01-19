from tkinter import filedialog
from PIL import Image
import os


def compress_and_resize_webp(input_folder, output_folder, quality, max_size):
    """
    Compresses and resizes all .webp images in the input folder without visible quality loss
    and saves them to the output folder.

    Parameters:
    - input_folder: The path to the folder containing input .webp files.
    - output_folder: The path to the folder to save the compressed .webp files.
    - quality: Compression quality (0-100), higher is better.
    - max_size: Maximum size for resizing images (width, height).

    Returns:
    - None
    """
    try:
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Loop through all .webp files in the input folder
        for file_name in os.listdir(input_folder):
            if file_name.lower().endswith(".webp"):
                input_path = os.path.join(input_folder, file_name)
                output_path = os.path.join(output_folder, file_name)

                # Open the original .webp image
                with Image.open(input_path) as img:
                    # Resize if the image is larger than max_size
                    if max_size != (0, 0):
                        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
                            img = img.resize(max_size)

                    # Save the compressed .webp image
                    img.save(output_path, "webp", quality=quality)
                    print(f"Image compressed and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print(
        "First of all, please choose an input folder where all the images are located."
    )
    input_folder = filedialog.askdirectory(title="Select Input Folder")
    if input_folder == "":
        print("Error: Input folder not found.")
        exit()

    print(
        "Now, please select an output folder, where the compressed images will be saved."
    )
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if output_folder == "":
        print("Error: Output folder not found.")
        exit()

    compression_quality = int(input("Enter the desired quality (0-100): "))
    if compression_quality > 100:
        compression_quality = 100
    elif compression_quality < 0:
        compression_quality = 0

    resizeAsk = input("Do you want to resize the images? (y/n): ")

    if resizeAsk == "y":
        max_size = (
            int(input("Enter the maximum width: ")),
            int(input("Enter the maximum height: ")),
        )

    # Check if the input folder exists
    if os.path.exists(input_folder):
        # Compress and resize all .webp images in the input folder
        if resizeAsk == "y":
            compress_and_resize_webp(
                input_folder,
                output_folder,
                quality=compression_quality,
                max_size=max_size,
            )
        else:
            compress_and_resize_webp(
                input_folder,
                output_folder,
                quality=compression_quality,
                max_size=(0, 0),
            )
    else:
        print("Error: Input folder not found.")
