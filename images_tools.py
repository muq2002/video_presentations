import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import shutil


def compare_images(imageA, imageB):
    imageA_gray = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB_gray = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    score, _ = ssim(imageA_gray, imageB_gray, full=True)
    return score


def remove_similar_images(output_folder, similarity_threshold=0.9):
    input_folder = "./videos/output_images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [
        f
        for f in os.listdir(input_folder)
        if os.path.isfile(os.path.join(input_folder, f))
    ]
    unique_images = []

    for i, image_file in enumerate(image_files):
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        is_unique = True
        for unique_image in unique_images:
            unique_image_path = os.path.join(output_folder, unique_image)
            unique_image_data = cv2.imread(unique_image_path)

            similarity_score = compare_images(image, unique_image_data)

            if similarity_score >= similarity_threshold:
                is_unique = False
                break

        if is_unique:
            shutil.move(image_path, os.path.join(output_folder, image_file))
            unique_images.append(image_file)
        else:
            os.remove(image_path)

    print(f"Finished processing. Unique images are stored in '{output_folder}'.")
