import os
from PIL import Image


def convert_images_to_pdf(input_folder, output_pdf):
    image_files = [
        f
        for f in os.listdir(input_folder)
        if f.endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff"))
    ]
    image_files.sort()

    image_list = []

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)

        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        image_list.append(image)

    if image_list:
        first_image = image_list.pop(0)
        first_image.save(output_pdf, save_all=True, append_images=image_list)
        print(f"PDF created successfully: {output_pdf}")
    else:
        print("No images found in the input folder.")
