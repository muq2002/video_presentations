import os
from PIL import Image

def convert_images_to_pdf(input_folder, output_pdf):
    # List all files in the directory
    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    image_files.sort()  # Sort files to maintain order if needed

    # List to store image objects
    image_list = []

    # Open each image and append it to the image list
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)
        
        # Convert image to RGB mode (required for PDF conversion)
        if image.mode in ('RGBA', 'P'):
            image = image.convert('RGB')
        
        image_list.append(image)

    # Save the first image as the base PDF, appending the rest as pages
    if image_list:
        first_image = image_list.pop(0)
        first_image.save(output_pdf, save_all=True, append_images=image_list)
        print(f"PDF created successfully: {output_pdf}")
    else:
        print("No images found in the input folder.")

# Usage
input_folder = 'results'  # Folder containing the images
output_pdf = 'output.pdf'  # Output PDF file name

convert_images_to_pdf(input_folder, output_pdf)
