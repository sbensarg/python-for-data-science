
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the given path, prints its shape, and returns
    its pixel data in RGB format as a NumPy array.

    Args:
        path (str): The path to the image file.

    Returns:
        np.ndarray: The image data as a NumPy array in RGB format.

    Raises:
        FileNotFoundError: If the file doesn't exist.
        OSError: If the file is not a valid image or unsupported format.
    """
    try:
        # The 'with' statement is used to ensure the file is properly closed after use.
        with Image.open(path) as img:
            if img.format not in ["JPEG", "JPG"]:
                raise OSError(f"Unsupported image format: {img.format}")
            rgb_img = img.convert("RGB")
            img_array = np.array(rgb_img)
            print(f"The shape of image is: {img_array.shape}")
            return img_array
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except OSError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None
