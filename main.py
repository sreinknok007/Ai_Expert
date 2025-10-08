
import cv2

import numpy as np
import matplotlib.pyplot as plt



def apply_color_filter(image, filter_type):

    """Apply the specified color filter to the image."""

    # Create a copy of the image to avoid modifying the original

    filtered_image = image.copy()


    if filter_type == "red_tint":

        # Remove blue and green channels for red tint

        filtered_image[:, :, 1] = 0  # Green channel to 0

        filtered_image[:, :, 2] = 0  # Blue channel to 0


    elif filter_type == "blue_tint":

        # Remove red and green channels for blue tint

        filtered_image[:, :, 1] = 0  # Green channel to 0

        filtered_image[:, :, 0] = 0  # Red channel to 0


    elif filter_type == "green_tint":

        # Remove blue and red channels for green tint

        filtered_image[:, :, 2] = 0  # Blue channel to 0

        filtered_image[:, :, 0] = 0  # Red channel to 0


    elif filter_type == "increase_red":

        # Increase the intensity of the red channel

        filtered_image[:, :, 0] = cv2.add(filtered_image[:, :, 0], 50)  # Increase red channel


    elif filter_type == "decrease_blue":

        # Decrease the intensity of the blue channel

        filtered_image[:, :, 2] = cv2.subtract(filtered_image[:, :, 2], 50)  # Decrease blue channel


    return filtered_image


# Load the image

image_path = 'Naru.jpg'  # Provide your image path

image = cv2.imread(image_path)
image = cv2.imread('Naru.jpg')


if image is None:

    print("Error: Image not found!")

else:

    filter_type = "original"  # Default filter type


    print("Press the following keys to apply filters:")

    print("r - Red Tint")

    print("b - Blue Tint")

    print("g - Green Tint")

    print("i - Increase Red Intensity")

    print("d - Decrease Blue Intensity")

    print("q - Quit")



    while True:

        key = input("Enter Key to process: r/b/g/i/d/q")




        # Map key presses to filters

        if key == 'r':

             filter_type = "red_tint"
             # Apply the selected filter
             filtered_image = apply_color_filter(image, filter_type)
            # Display the filtered image
             plt.title(f"Filtered Image - {filter_type}")
             plt.imshow(filtered_image)
             plt.show()

        elif key == 'b':

            filter_type = "blue_tint"
            # Apply the selected filter
            filtered_image = apply_color_filter(image, filter_type)
            # Display the filtered image
            plt.title(f"Filtered Image - {filter_type}")
            plt.imshow(filtered_image)
            plt.show()

        elif key == 'g':

            filter_type = "green_tint"
            # Apply the selected filter
            filtered_image = apply_color_filter(image, filter_type)
            # Display the filtered image
            plt.title(f"Filtered Image - {filter_type}")
            plt.imshow(filtered_image)
            plt.show()

        elif key == 'i':

            filter_type = "increase_red"
            # Apply the selected filter
            filtered_image = apply_color_filter(image, filter_type)
            # Display the filtered image
            plt.title(f"Filtered Image - {filter_type}")
            plt.imshow(filtered_image)
            plt.show()

        elif key == 'd':

            filter_type = "decrease_blue"
            # Apply the selected filter
            filtered_image = apply_color_filter(image, filter_type)
            # Display the filtered image
            plt.title(f"Filtered Image - {filter_type}")
            plt.imshow(filtered_image)
            plt.show()

        elif key == 'q':

            print("Exiting...")

            break

        else:

            print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")
