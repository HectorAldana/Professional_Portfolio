import cv2
import numpy as np
import math

def bilinear_interpolate(image, x, y):
    # Grab the dimensions of the image
    height, width, _ = image.shape

    # Calculate the coordinates of the four neighbors
    x1, y1 = int(x), int(y)
    x2, y2 = min(x1 + 1, width - 1), min(y1 + 1, height - 1)

    # Calculate the differences from the original coordinates
    dx, dy = x - x1, y - y1

    # Get pixel values of four neighbors
    q11 = image[y1, x1]
    q21 = image[y1, x2]
    q12 = image[y2, x1]
    q22 = image[y2, x2]

    # Perform the interpolation
    b1 = q11 * (1 - dx) + q21 * dx
    b2 = q12 * (1 - dx) + q22 * dx
    interpolated_value = b1 * (1 - dy) + b2 * dy

    return np.clip(interpolated_value, 0, 255)

def rotate_image_color(image_path, angle):
    # Load the color image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    height, width = image.shape[:2]

    # Create a new image with the same size but filled with zeros (black background)
    rotated_image = np.zeros((height, width, 3), np.uint8)

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

            # Perform bilinear interpolation
            if 0 <= new_x < width and 0 <= new_y < height:
                rotated_image[y, x] = bilinear_interpolate(image, new_x, new_y)

    # Display the original and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Use the function
rotate_image_color('Sheep.jpg', -45)  # Replace with your image path and desired rotation angle
