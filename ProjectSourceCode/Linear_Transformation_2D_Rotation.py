import cv2
import numpy as np
import math

def rotate_image_manual(image_path, angle):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load as grayscale for simplicity
    height, width = image.shape

    # Create a new image with the same size but filled with zeros (black)
    rotated_image = np.zeros((height, width), np.uint8)

    # Calculate the center of the image
    center_y, center_x = height // 2, width // 2

    # Convert the angle to radians
    angle_rad = math.radians(angle)

    # Create the rotation matrix
    rotation_matrix = np.array([
        [math.cos(angle_rad), -math.sin(angle_rad)],
        [math.sin(angle_rad), math.cos(angle_rad)]
    ])

    # Apply the transformation to each pixel
    for y in range(height):
        for x in range(width):
            # Translate the pixel to origin and then rotate
            yp = y - center_y
            xp = x - center_x
            new_x, new_y = np.matmul(rotation_matrix, np.array([xp, yp]))

            # Translate back from the origin
            new_x += center_x
            new_y += center_y

            # If the new position is within the bounds of the image, set the pixel
            if 0 <= new_x < width and 0 <= new_y < height:
                rotated_image[int(new_y), int(new_x)] = image[y, x]

    # Display the original and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Use the function
rotate_image_manual('path_to_your_image.jpg', 45)  # Replace with your image path and desired rotation angle
