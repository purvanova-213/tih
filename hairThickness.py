import cv2
import numpy as np

def measure_hair_thickness(image_path):
    # Load the hair scalp image
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to segment the hair strands
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Find contours of hair strands
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Calculate the cumulative thickness and count of hair strands
    cumulative_thickness = 0
    strand_count = 0
    
    for contour in contours:
        # Calculate the bounding rectangle of the contour
        x, y, w, h = cv2.boundingRect(contour)
        
        # Calculate the thickness of the hair strand (considering width)
        thickness = w
        
        cumulative_thickness += thickness
        strand_count += 1
    
    # Calculate the average hair thickness
    average_thickness = cumulative_thickness / strand_count
    
    return average_thickness

# Example usage
image_path = 'hair_image.jpeg'
average_hair_thickness = measure_hair_thickness(image_path)
print("Average Hair Thickness:", average_hair_thickness)
