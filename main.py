# main.py

import os
import argparse
from video_tools import video_to_frames
from images_tools import ImageProcessor  # Import the class directly
from convert_to_pdf import convert_images_to_pdf
from download_youtube import YouTubeDownloader
from urllib.parse import urlparse


def is_youtube_url(url):
    """Check if the provided string is a YouTube URL."""
    try:
        parsed = urlparse(url)
        return "youtube.com" in parsed.netloc or "youtu.be" in parsed.netloc
    except:
        return False


def process_video(video_path, output_folder, interval, remove_similar, create_pdf):
    """Process video with frame extraction and optional features."""
    try:
        os.makedirs(output_folder, exist_ok=True)

        # Extract frames
        print(f"Extracting frames every {interval} seconds...")
        video_to_frames(video_path, output_folder, interval)

        # Remove similar images if requested
        if remove_similar:
            print("Removing similar images...")
            image_processor = ImageProcessor(similarity_threshold=0.9)
            unique_folder = os.path.join(output_folder, "unique")
            unique_count, removed_count = image_processor.remove_similar_images(
                output_folder, unique_folder
            )
            print(
                f"Removed {removed_count} similar images, kept {unique_count} unique images"
            )
            output_folder = unique_folder  # Update output folder for PDF creation

        # Convert to PDF if requested
        if create_pdf:
            pdf_path = os.path.join(os.path.dirname(video_path), "output.pdf")
            print("Converting images to PDF...")
            convert_images_to_pdf(output_folder, pdf_path)
            print(f"PDF created at: {pdf_path}")

    except Exception as e:
        print(f"Error processing video: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Process a video (local file or YouTube URL) to extract frames, remove similar images, and convert to PDF."
    )
    parser.add_argument(
        "-v", "--video", required=True, help="Path to local video file or YouTube URL"
    )
    parser.add_argument(
        "-o", "--output", default="images", help="Output folder for extracted images"
    )
    parser.add_argument(
        "-i",
        "--interval",
        type=int,
        default=5,
        help="Interval in seconds between frames to extract",
    )
    parser.add_argument(
        "-r",
        "--remove_similar",
        action="store_true",
        help="Remove similar images after extraction",
    )
    parser.add_argument(
        "-p", "--pdf", action="store_true", help="Convert extracted images to PDF"
    )
    parser.add_argument(
        "-d",
        "--download_path",
        default="./downloads",
        help="Path to save downloaded YouTube videos",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=float,
        default=0.9,
        help="Similarity threshold for image comparison (0.0 to 1.0)",
    )

    args = parser.parse_args()

    # Process YouTube URL or local file
    if is_youtube_url(args.video):
        print("YouTube URL detected. Starting download...")
        downloader = YouTubeDownloader()

        video_info = downloader.get_video_info(args.video)
        if video_info:
            print(f"\nVideo Information:")
            print(f"Title: {video_info['title']}")
            print(f"Duration: {video_info['duration']} seconds")
            print(f"Uploader: {video_info['uploader']}")

            video_path, _ = downloader.download_youtube_video(
                args.video, args.download_path
            )
            if not video_path:
                print("Failed to download video.")
                return
        else:
            print("Failed to get video information.")
            return
    else:
        print("Local video file detected.")
        video_path = args.video
        if not os.path.exists(video_path):
            print(f"Error: Video file not found at {video_path}")
            return

    # Create output folder and process video
    output_folder = os.path.join(os.path.dirname(video_path), args.output)
    process_video(
        video_path, output_folder, args.interval, args.remove_similar, args.pdf
    )

    # Print summary
    print("\nCreated/Modified files:")
    for root, _, files in os.walk(output_folder):
        for file in files:
            print(os.path.join(root, file))


if __name__ == "__main__":
    main()
