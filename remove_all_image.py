import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import shutil

# Function to calculate similarity between two images
def compare_images(imageA, imageB):
    # Convert images to grayscale
    imageA_gray = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB_gray = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    
    # Compute SSIM between two images
    score, _ = ssim(imageA_gray, imageB_gray, full=True)
    return score

# Function to remove similar images and move unique images to a new folder
def remove_similar_images(input_folder, output_folder, similarity_threshold=0.9):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get list of image files in the folder
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    unique_images = []
    
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)
        
        is_unique = True
        for unique_image in unique_images:
            unique_image_path = os.path.join(output_folder, unique_image)
            unique_image_data = cv2.imread(unique_image_path)
            
            # Compare current image with unique images
            similarity_score = compare_images(image, unique_image_data)
            
            if similarity_score >= similarity_threshold:
                is_unique = False
                break
        
        if is_unique:
            # If the image is unique, move it to the output folder
            shutil.move(image_path, os.path.join(output_folder, image_file))
            unique_images.append(image_file)
        else:
            # If not unique, remove the image
            os.remove(image_path)

    print(f"Finished processing. Unique images are stored in '{output_folder}'.")

# Usage
input_folder = './videos/images'  # Replace with your input folder path
output_folder = 'results'  # Output folder for unique images
similarity_threshold = 0.9  # Threshold for similarity (1.0 is identical)

remove_similar_images(input_folder, output_folder, similarity_threshold)
