import cv2

# Load the trichoscopy image in grayscale
image = cv2.imread('hair_image.jpeg', cv2.IMREAD_GRAYSCALE)

# Apply adaptive thresholding to segment hair follicle openings
_, threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Apply morphological operations to enhance the hair follicle openings
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
morph = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)

# Find contours of hair follicle openings
contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw red circles around the hair follicle openings
for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    center = (int(x + w / 2), int(y + h / 2))
    radius = int((w + h) / 4)
    cv2.circle(image, center, radius, (0, 0, 255), 2)

# Display the resulting image
cv2.imshow('Hair Follicle Openings', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

