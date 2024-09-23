import cv2
import numpy as np

# Load the image
image_path = './bonomala.png'
image = cv2.imread(image_path)

# Display the image to manually determine the pixel length of the 10m scale
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'Clicked at: ({x}, {y})')
        points.append((x, y))
        # Draw a small circle where clicked
        cv2.circle(image, (x, y), 3, (0, 255, 0), -1)
        cv2.imshow("Image", image)

# Show the image and capture the pixel positions of the 10-meter scale
points = []
cv2.imshow("Image", image)
cv2.setMouseCallback("Image", click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Calculate the pixel distance between the two points of the scale
if len(points) == 2:
    pixel_distance = np.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2)
    print(f"Pixel distance for 10 meters: {pixel_distance} pixels")

    # Given that this distance corresponds to 10 meters, calculate the meters per pixel
    meters_per_pixel = 10 / pixel_distance
    print(f"1 pixel = {meters_per_pixel} meters")
else:
    print("Please click on exactly two points on the 10-meter scale.")