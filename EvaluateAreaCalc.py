import cv2
import numpy as np

# Load the image
image_path = './bonomala.png'
image = cv2.imread(image_path)

# Known reference area in meters squared (adjust this to match the known area in real life)
reference_area_meters_squared = 1449.59  # Example: known reference area in meters squared

# Initialize variables
points = []
polygon_complete = False

# Function to capture mouse clicks and store polygon points
def draw_polygon(event, x, y, flags, param):
    global points, polygon_complete

    if event == cv2.EVENT_LBUTTONDOWN and not polygon_complete:
        points.append((x, y))
        cv2.circle(image, (x, y), 3, (0, 255, 0), -1)  # Draw points
        cv2.imshow("Image", image)

    elif event == cv2.EVENT_RBUTTONDOWN and len(points) > 2:
        # When the right mouse button is clicked, close the polygon
        polygon_complete = True
        cv2.polylines(image, [np.array(points)], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.imshow("Image", image)

# Display the image and set the mouse callback
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", draw_polygon)

# Wait for the user to draw the polygon
cv2.waitKey(0)
cv2.destroyAllWindows()

# Ensure we have a completed polygon
if polygon_complete:
    # Convert the list of points to a contour (OpenCV uses contours for polygon shapes)
    contour = np.array(points)

    # Calculate the pixel area of the polygon
    pixel_area = cv2.contourArea(contour)
    print(f"Pixel area: {pixel_area} pixels")
    
    # Calculate meters per pixel using the reference area
    meters_per_pixel = (reference_area_meters_squared / pixel_area) ** 0.5
    print(f"Recalculated meters per pixel: {meters_per_pixel} meters")

    # Calculate the estimated area using the recalculated meters per pixel
    area_in_meters_squared = pixel_area * (meters_per_pixel ** 2)
    print(f"Estimated area using recalculated scale: {area_in_meters_squared} meters squared")
    
    # Calculate accuracy (percentage)
    accuracy = (1 - abs(area_in_meters_squared - reference_area_meters_squared) / reference_area_meters_squared) * 100
    print(f"Accuracy: {accuracy:.2f}%")

    # Optionally, you can print out an error percentage (100% - accuracy)
    error_percentage = 100 - accuracy
    print(f"Error percentage: {error_percentage:.2f}%")

else:
    print("Please draw a polygon to calculate the area.")
