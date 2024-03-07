import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = 'C:\\Users\\sisir\\Downloads\\dataset23\\Healthy\\PAC_69_DN9_.jpg'
image = cv2.imread(image_path)

# Define the ROI coordinates (format: top-left corner (x, y), bottom-right corner (x, y))
roi_coordinates = ((100, 50), (300, 250))

# Extract the ROI from the image
roi = image[roi_coordinates[0][1]:roi_coordinates[1][1], roi_coordinates[0][0]:roi_coordinates[1][0]]

# Calculate the center of the ROI
center_x = (roi_coordinates[0][0] + roi_coordinates[1][0]) // 2
center_y = (roi_coordinates[0][1] + roi_coordinates[1][1]) // 2

# Calculate the new coordinates to center the view
view_width = 200  # Adjust as needed
view_height = 200  # Adjust as needed

view_x = max(0, center_x - view_width // 2)
view_y = max(0, center_y - view_height // 2)

# Set the region to display
view = image[view_y:view_y + view_height, view_x:view_x + view_width]

# Display the original image and the centered view side by side
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(view, cv2.COLOR_BGR2RGB))
plt.title('View')

plt.show()
