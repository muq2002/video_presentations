import os
import argparse
from download_youtube import YouTubeDownloader

def format_duration(seconds):
    """Convert duration in seconds to HH:MM:SS format."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def main():
    parser = argparse.ArgumentParser(
        description="Download YouTube videos and extract information."
    )
    parser.add_argument(
        "-u", "--url",
        required=True,
        help="YouTube video URL"
    )
    parser.add_argument(
        "-o", "--output",
        default="./downloads",
        help="Output directory for downloaded videos"
    )
    parser.add_argument(
        "-i", "--info-only",
        action="store_true",
        help="Only show video information without downloading"
    )

    args = parser.parse_args()

    # Initialize downloader
    downloader = YouTubeDownloader()

    # Get video information
    print("Fetching video information...")
    video_info = downloader.get_video_info(args.url)

    if video_info:
        print("\nVideo Information:")
        print(f"Title: {video_info['title']}")
        print(f"Uploader: {video_info['uploader']}")
        if isinstance(video_info['duration'], (int, float)):
            print(f"Duration: {format_duration(video_info['duration'])}")
        print(f"Views: {video_info['view_count']:,}")
        print(f"Likes: {video_info['like_count']:,}")
        print(f"Upload Date: {video_info['upload_date']}")
        if video_info['tags']:
            print(f"Tags: {', '.join(video_info['tags'][:5])}...")
        print("\nDescription:")
        print(video_info['description'][:200] + "..." if len(video_info['description']) > 200 else video_info['description'])

        # Download video if not info-only mode
        if not args.info_only:
            print("\nStarting download...")
            video_path, _ = downloader.download_youtube_video(args.url, args.output)

            if video_path:
                print("\nCreated/Modified files:")
                for root, _, files in os.walk(args.output):
                    for file in files:
                        print(os.path.join(root, file))
    else:
        print("Failed to retrieve video information.")

if __name__ == "__main__":
    main()