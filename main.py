import os
import argparse
from video_tools import video_to_frames
from images_tools import remove_similar_images
from convert_to_pdf import convert_images_to_pdf


def main():
    parser = argparse.ArgumentParser(
        description="Process a video to extract frames, remove similar images, and convert to PDF."
    )
    parser.add_argument("-v", "--video", required=True, help="Path to the video file.")
    parser.add_argument(
        "-o", "--output", default="images", help="Output folder for extracted images."
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=5,
        help="Interval in seconds between frames to extract.",
    )
    parser.add_argument(
        "-r",
        "--remove_similar",
        action="store_true",
        help="Remove similar images after extraction.",
    )
    parser.add_argument(
        "-p", "--pdf", action="store_true", help="Convert extracted images to PDF."
    )

    args = parser.parse_args()

    output_folder = os.path.join(os.path.dirname(args.video), args.output)
    os.makedirs(output_folder, exist_ok=True)

    video_to_frames(args.video, output_folder, args.interval)

    if args.remove_similar:
        remove_similar_images(output_folder)

    # Optionally convert images to PDF
    if args.pdf:
        pdf_path = os.path.join(os.path.dirname(args.video), "output.pdf")
        convert_images_to_pdf(output_folder, pdf_path)
        print(f"PDF created at: {pdf_path}")


if __name__ == "__main__":
    main()
