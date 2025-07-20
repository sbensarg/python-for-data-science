import matplotlib.pyplot as plt
from load_image import ft_load


def display_image(img, cmap="gray"):
    """Display the image using matplotlib
    plt.imshow(img, cmap=cmap)
    plt.show()

    Parameters:
        img (np.ndarray): The image to display.
        cmap (str): The color map to use.

    Returns:
        None
    """
    plt.imshow(img, cmap=cmap)
    plt.show()


def zoom(image):
    """Return a zoomed region of the image with only the red channel.
    Parameters:
        image (np.ndarray): The image to zoom.
    Returns:
        np.ndarray: The zoomed image.
    """
    return image[100:500, 450:850, 0:1]


def main():
    """Main function to load an image, zoom into a region, and display it."""
    try:
        img = ft_load("animal.jpeg")
        print("The shape of image is:", img.shape)
        print(img)

        zoomed = zoom(img)
        print("New shape after slicing:", zoomed.shape, "or", zoomed.shape[:2])
        print(zoomed)

        display_image(zoomed)

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
