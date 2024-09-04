import yt_dlp as youtube_dl


def download_youtube_video(url, save_path="."):
    try:
        # Set up the download options
        ydl_opts = {
            "outtmpl": f"{save_path}/%(title)s.%(ext)s",  # Save as the title of the video
            "format": "best",  # Download the best available quality
        }

        # Download the video
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Download completed! Video saved to: {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_video_info(url):
    try:
        # Set up options to extract information
        ydl_opts = {
            "skip_download": True,  # Do not download the video
        }

        # Extract video information
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)

        # Display the extracted information
        video_info = {
            "title": info_dict.get("title", "N/A"),
            "uploader": info_dict.get("uploader", "N/A"),
            "duration": info_dict.get("duration", "N/A"),
            "view_count": info_dict.get("view_count", "N/A"),
            "like_count": info_dict.get("like_count", "N/A"),
            "dislike_count": info_dict.get("dislike_count", "N/A"),
            "upload_date": info_dict.get("upload_date", "N/A"),
            "description": info_dict.get("description", "N/A"),
            "tags": info_dict.get("tags", []),
        }

        return video_info
    except Exception as e:
        print(f"An error occurred while retrieving video information: {e}")
        return None


# Example usage
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=-i3NQ-by2b8"  # Replace with your desired video URL
    download_path = "./downloads"  # Replace with your desired save path

    # Download the video
    download_youtube_video(video_url, download_path)

    # Get video information
    info = get_video_info(video_url)
    if info:
        print("\nVideo Information:")
        for key, value in info.items():
            print(f"{key.capitalize()}: {value}")
