from PIL import Image


def compress_image(input_path, output_path, quality):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, quality=quality)
        return True
    except Exception as e:
        print(f"Error compressing image: {e}")
        return False
