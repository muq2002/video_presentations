import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
import shutil
from tqdm import tqdm


class ImageProcessor:
    def __init__(self, similarity_threshold=0.9):
        self.similarity_threshold = similarity_threshold

    def compare_images(self, imageA, imageB):
        """
        Compare two images using Structural Similarity Index (SSIM).

        Args:
            imageA: First image
            imageB: Second image

        Returns:
            float: Similarity score between 0 and 1
        """
        try:
            # Convert images to grayscale
            imageA_gray = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
            imageB_gray = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

            # Ensure images are the same size
            if imageA_gray.shape != imageB_gray.shape:
                height = min(imageA_gray.shape[0], imageB_gray.shape[0])
                width = min(imageA_gray.shape[1], imageB_gray.shape[1])
                imageA_gray = cv2.resize(imageA_gray, (width, height))
                imageB_gray = cv2.resize(imageB_gray, (width, height))

            # Calculate SSIM
            score, _ = ssim(imageA_gray, imageB_gray, full=True)
            return score
        except Exception as e:
            print(f"Error comparing images: {e}")
            return 0.0

    def remove_similar_images(self, input_folder, output_folder):
        """
        Remove similar images from input folder and move unique ones to output folder.

        Args:
            input_folder: Path to folder containing input images
            output_folder: Path to folder where unique images will be stored

        Returns:
            tuple: (number of unique images, number of removed images)
        """
        try:
            # Create output folder if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)

            # Get list of image files
            image_files = [
                f
                for f in os.listdir(input_folder)
                if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff"))
                and os.path.isfile(os.path.join(input_folder, f))
            ]

            if not image_files:
                print(f"No image files found in {input_folder}")
                return 0, 0

            unique_images = []
            removed_count = 0

            print(f"Processing {len(image_files)} images...")

            # Process images with progress bar
            for image_file in tqdm(image_files, desc="Processing images"):
                image_path = os.path.join(input_folder, image_file)

                try:
                    image = cv2.imread(image_path)
                    if image is None:
                        print(f"Warning: Could not read image {image_file}")
                        continue

                    is_unique = True

                    # Compare with existing unique images
                    for unique_image in unique_images:
                        unique_image_path = os.path.join(output_folder, unique_image)
                        unique_image_data = cv2.imread(unique_image_path)

                        similarity_score = self.compare_images(image, unique_image_data)

                        if similarity_score >= self.similarity_threshold:
                            is_unique = False
                            break

                    if is_unique:
                        shutil.move(image_path, os.path.join(output_folder, image_file))
                        unique_images.append(image_file)
                    else:
                        os.remove(image_path)
                        removed_count += 1

                except Exception as e:
                    print(f"Error processing {image_file}: {e}")
                    continue

            print(f"\nProcessing complete:")
            print(f"- Unique images: {len(unique_images)}")
            print(f"- Removed duplicates: {removed_count}")
            print(f"- Unique images stored in: {output_folder}")

            return len(unique_images), removed_count

        except Exception as e:
            print(f"Error in remove_similar_images: {e}")
            return 0, 0
