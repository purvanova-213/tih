import cv2
# Load the image
img = cv2.imread('hair_image.jpeg')
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply a threshold
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# Apply morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
# Find the hair contours
contours, hierarchy = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Count the hair
hair_count = len(contours)
print("Number of hairs:", hair_count)
cv2.imshow('Normal Image',img)
cv2.imshow('Gray Image',gray)
cv2.imshow('Threshold Image',thresh)
cv2.waitKey(0)