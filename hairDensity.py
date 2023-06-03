import cv2

# Load the image
image = cv2.imread('hair_image.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply image preprocessing if needed (e.g., image enhancement, noise reduction)
enhanced_image = cv2.equalizeHist(image)

# Define the measurement area coordinates (x, y, width, height)
x = 100
y = 100
width = 100
height = 100

# Crop the image to the defined measurement area
measurement_area = enhanced_image[y:y+height, x:x+width]

# Apply thresholding or other techniques to separate hair from the background if needed

# Count the number of hairs
num_hairs = cv2.countNonZero(measurement_area)

# Calculate the hair density
area = width * height  # Size of the measurement area in square pixels
hair_density = num_hairs / area

# Print the hair density
print("Hair Density:", hair_density, "hairs/pixel^2")

import cv2

# Load the image
image = cv2.imread('hair_image.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply image preprocessing if needed (e.g., image enhancement, noise reduction)

# Define the measurement area coordinates (x, y, width, height)
x = 100
y = 100
width = 100
height = 100

# Crop the image to the defined measurement area
measurement_area = enhanced_image[y:y+height, x:x+width]

# Apply thresholding or other techniques to separate hair from the background if needed

# Count the number of hairs
num_hairs = cv2.countNonZero(measurement_area)

# Calculate the hair density
area = width * height  # Size of the measurement area in square pixels
hair_density = num_hairs / area

# Print the hair density
print("Hair Density:", hair_density, "hairs/pixel^2")

