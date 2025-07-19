"""
tester.py
This script tests the ft_load function from load_image.py with a sample image.
"""

from load_image import ft_load


def main():
    """
    Main function to test ft_load with an image path.
    """
    image_array = ft_load("tester.py")
    if image_array is not None:
        print(image_array)


if __name__ == "__main__":
    main()
