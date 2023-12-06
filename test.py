import cv2
import numpy as np

def calculate_orange_rooftop_area(image_path, min_contour_area, pixel_size):
    image = cv2.imread(image_path)

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for orange color in HSV
    lower_orange = np.array([0, 60, 60])
    upper_orange = np.array([30, 255, 255])

    # Create a mask for the orange color
    orange_mask = cv2.inRange(hsv_image, lower_orange, upper_orange)

    contours, _ = cv2.findContours(orange_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    total_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)

        # Exclude small contours based on the provided threshold
        if area >= min_contour_area:
            total_area += area

            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    # Display the original image with contours
    cv2.imshow('Original Image with Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Convert the total area from square pixels to square meters
    total_area_m2 = total_area * pixel_size

    return total_area_m2

if __name__ == "__main__":
    min_contour_area = 1500 #Replace this due to the image
    image_path = 'path/image.jpeg'
    
    pixel_size = 0.0001  # Replace this value with the actual pixel size of your image
    
    total_rooftop_area = calculate_orange_rooftop_area(image_path, min_contour_area, pixel_size)
    print(f'Total Orange Rooftop Area: {total_rooftop_area} square meters')
