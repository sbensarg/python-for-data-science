from PIL import Image
import numpy as np


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    Subtracts each pixel value from 255 to create negative effect.

    Parameters:
        array (np.ndarray): The input image array in RGB format

    Returns:
        np.ndarray: The inverted image array
    """
    try:
        # Use subtraction: 255 - original_value = inverted_value
        # This creates a "negative" effect where black becomes white, etc.
        inverted_array = 255 - array

        # Convert numpy array back to PIL Image and display it
        Image.fromarray(inverted_array).show()

        # Return the inverted array
        return inverted_array

    except Exception as e:
        print(f"Error in ft_invert: {e}")
        return array  # Return original if error occurs


def ft_red(array) -> np.ndarray:
    """
    Keeps only the red channel, sets green and blue to zero.
    Uses multiplication to zero out unwanted channels.

    Parameters:
        array (np.ndarray): The input image array in RGB format

    Returns:
        np.ndarray: Image with only red channel visible
    """
    try:
        # Create a copy of the original array to avoid modifying it
        red_filtered = array.copy()

        # Method 1: Using multiplication (allowed operator)
        # Multiply red channel by 1 (keeps it), others by 0 (zeros them)
        red_filtered = red_filtered * [1, 0, 0]

        # Convert to proper data type for display
        red_filtered = red_filtered.astype(np.uint8)

        # Display the red-filtered image
        Image.fromarray(red_filtered).show()

        return red_filtered

    except Exception as e:
        print(f"Error in ft_red: {e}")
        return array


def ft_green(array) -> np.ndarray:
    """
    Keeps only the green channel, sets red and blue to zero.
    Uses subtraction to zero out unwanted channels.

    Parameters:
        array (np.ndarray): The input image array in RGB format

    Returns:
        np.ndarray: Image with only green channel visible
    """
    try:
        # Create a copy to avoid modifying original
        green_filtered = array.copy()

        # Method using subtraction (allowed operator)
        # Subtract red channel from itself to make it 0
        green_filtered[:, :, 0] = green_filtered[:, :, 0] - green_filtered[:, :, 0]

        # Subtract blue channel from itself to make it 0
        green_filtered[:, :, 2] = green_filtered[:, :, 2] - green_filtered[:, :, 2]

        # Green channel (:, :, 1) remains unchanged

        # Display the green-filtered image
        Image.fromarray(green_filtered).show()

        return green_filtered

    except Exception as e:
        print(f"Error in ft_green: {e}")
        return array


def ft_blue(array) -> np.ndarray:
    """
    Keeps only the blue channel, sets red and green to zero.
    Uses only assignment operator.

    Parameters:
        array (np.ndarray): The input image array in RGB format

    Returns:
        np.ndarray: Image with only blue channel visible
    """
    try:
        # Create an array of zeros with same shape as input
        # This gives us a black image to start with
        blue_filtered = np.zeros_like(array)

        # Only assignment allowed, so we copy just the blue channel
        # Leave red (channel 0) and green (channel 1) as zeros
        blue_filtered[:, :, 2] = array[:, :, 2]  # Copy blue channel only

        # Display the blue-filtered image
        Image.fromarray(blue_filtered).show()

        return blue_filtered

    except Exception as e:
        print(f"Error in ft_blue: {e}")
        return array


def ft_grey(array) -> np.ndarray:
    """
    Converts image to grayscale by averaging RGB values.
    Uses division to calculate the average of the three color channels.

    Parameters:
        array (np.ndarray): The input image array in RGB format

    Returns:
        np.ndarray: Grayscale version of the image
    """
    try:
        # Calculate grayscale by averaging the three color channels
        # Add all three channels together, then divide by 3
        gray_values = (array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) / 3

        # Convert to integer type for proper display
        gray_values = gray_values.astype(np.uint8)

        # Create RGB array where all three channels have the same gray value
        # This creates a proper grayscale image that can be displayed in color format
        gray_filtered = np.zeros_like(array)
        gray_filtered[:, :, 0] = gray_values  # Red channel = gray value
        gray_filtered[:, :, 1] = gray_values  # Green channel = gray value  
        gray_filtered[:, :, 2] = gray_values  # Blue channel = gray value

        # Display the grayscale image
        Image.fromarray(gray_filtered).show()

        return gray_filtered

    except Exception as e:
        print(f"Error in ft_grey: {e}")
        return array


if __name__ == "__main__":
    pass
