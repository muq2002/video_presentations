import os
import yt_dlp as youtube_dl


class YouTubeDownloader:
    def __init__(self):
        self.default_download_path = "./downloads"

    def download_youtube_video(self, url, save_path=None):
        """Download YouTube video and return the path to downloaded file."""
        if save_path is None:
            save_path = self.default_download_path

        try:
            os.makedirs(save_path, exist_ok=True)

            ydl_opts = {
                "outtmpl": f"{save_path}/%(title)s.%(ext)s",
                "format": "best",
                "quiet": False,
                "no_warnings": False,
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                video_path = os.path.join(save_path, f"{info['title']}.{info['ext']}")
                print(f"Download completed! Video saved to: {video_path}")
                return video_path, info

        except Exception as e:
            print(f"An error occurred during download: {e}")
            return None, None

    def get_video_info(self, url):
        """Get video information without downloading."""
        try:
            ydl_opts = {
                "skip_download": True,
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)

            video_info = {
                "title": info_dict.get("title", "N/A"),
                "uploader": info_dict.get("uploader", "N/A"),
                "duration": info_dict.get("duration", "N/A"),
                "view_count": info_dict.get("view_count", "N/A"),
                "like_count": info_dict.get("like_count", "N/A"),
                "upload_date": info_dict.get("upload_date", "N/A"),
                "description": info_dict.get("description", "N/A"),
                "tags": info_dict.get("tags", []),
            }

            return video_info
        except Exception as e:
            print(f"An error occurred while retrieving video information: {e}")
            return None
